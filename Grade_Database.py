from argparse import ArgumentParser
import json
import pandas as pd
import sys

# What to add: Contributer of method, techniques displayed
class SchoolDatabase:
    """
    A database that stores and manages student information and grades.
    """

    def __init__(self, schoolname, file, classes=None, gpas=None):
        """
        Initializes the SchoolDatabase class with the school name and JSON file
        containing student information and grades. Converts the JSON file into a
        pandas DataFrame.

        Args:
            schoolname (str): The name of the school
            file (str): The path to the JSON file containing student information and grades
            classes (dict): A dictionary containing information about the classes taught at the school
            gpas (dict): A dictionary containing information about the GPAs of students at the school
        """
        self.schoolname = schoolname
        self.classes = classes
        self.gpas = gpas
        with open(file, "r") as f:
            data = json.load(f)
        self.df = pd.DataFrame.from_dict(data, orient="index")

    
    def similarclasses(self, class1, class2):
        """Find students who are taking both class1 and class2

        Args:
            class1 (str): the name of the first class
            class2 (str): the name of the second class

        Returns:
            A list of student names who are taking both class1 and class2
        """
        students_class1 = {x for x, row in self.df.iterrows() if row[class1] != ''}
        students_class2 = {x for x, row in self.df.iterrows() if row[class2] != ''}
        common_students = students_class1.intersection(students_class2)
        return [f"{self.df.loc[x, 'first_name']} {self.df.loc[x, 'last_name']}" for x in common_students]
  
  
    def honor_roll(self, threshold=3.0):
        """Find students with a GPA of at least the threshold

        Args:
            threshold (float): The minimum GPA required to be on the honor roll.

        Returns:
            A list of student names with a GPA of at least the threshold
        """
        grades = self.df.drop(['teacher', 'class'], axis=1).astype(float)
        gpa = grades.apply(lambda row: sum(row)/len(row)/20, axis=1)
        
        return gpa[gpa >= threshold].index.tolist()
    
    
    def classes_by_year(self):
        """Returns a DataFrame with information about the classes by year

        Returns:
            A pandas DataFrame with columns for the student's name, classes they
            took within a school year, and the teacher for each class they are taking.
        """
        classes_df = pd.DataFrame.from_dict(self.classes, orient='index').reset_index()
        classes_df.columns = ['class', 'teacher']

        students_df = self.df.stack().reset_index()
        students_df.columns = ['name', 'year', 'class']
        students_df = students_df[students_df['class'].str.len() > 0]

        students_df['classes'] = students_df['name'].apply(lambda x: sorted([class_name for class_name in self.df.loc[x, self.df.columns != 'grade'].values if class_name != '']))

        merged_df = pd.merge(students_df, classes_df, on='class', how='left')
        merged_df = merged_df[['name', 'year', 'class', 'teacher']]
        merged_df = merged_df.drop_duplicates().reset_index(drop=True)

        return merged_df
    
    def export_json(self, filename):
        """Exports the student information and grades to a JSON file.

        Args:
            filename (str): The name of the file to export to.
        """
        parser = argparse.ArgumentParser(description='Export student information to JSON file.')
        parser.add_argument('--indent', type=int, default=4, help='number of spaces for JSON indentation')
        args = parser.parse_args()

        data = self.df.to_dict(orient='index')
        with open(filename, 'w') as f:
            json.dump(data, f, indent=args.indent)




#Will a teacher also have composition of a student? Most likely combine 
# teachers and students file into one when done.
class Student:
    """ The following represents a student. The following student 
    will have components representing information about their school,
    alongside with their grades. Will be used in order to retrieve
    information about student in the SchoolDatabase class
    
    Attributes:
        name (str): The name of the student
        grades (dict): A dictionary containing the student's grades
        classname (list): A list containing the names of the classes the student is taking
    """
    
    def __init__(self, file, name):
        """ Initialize a student object
        """
        #text file will be potentially used to populate student info attribute section.
        self.grades = {}
        self.classname = []
        self.name = name
        index = 0
        with open (file, "r") as f:
            data = json.load(f)
            for years in data:
              for dicts in years:
                  while (index < 4):
                    #reason for such errors is needing to combine json files
                    for items in dicts:
                        if dicts[items] == self.name:
                            self.grades[items] = dicts[items]
                            self.classname.append(items)
                            index += 1
    
    def __displaygrades__(self):
        """Defines the common string representation of a student alongside
        with their grades.
        
        Returns:
        The string representation of the student and all their classes. """
        
        index = 0
        string = f"{self.name}: \n"
        for classes in self.grades:
            if classes > 90 and classes <= 100:
                string += f"{self.classname[index]} : A \n"
            elif classes > 80 and classes < 90:
                string += f"{self.classname[index]} : B \n"
            elif classes > 70 and classes < 80:
                string += f"{self.classname[index]} : C \n"
            elif classes > 60 and classes < 70:
                string += f"{self.classname[index]} : D \n"
            elif classes < 60:
                string += f"{self.classname[index]} : F \n"
            index += 1
        
        return string
        
        
    def toletter(self):
        """ Returns the letter grade for the student

        Returns:
            str: The letter grade for the student
        """
        avg_grade = sum(self.grades.values()) / len(self.grades)

        if avg_grade > 90 and avg_grade <= 100:
            return 'A'
        elif avg_grade > 80 and avg_grade < 90:
            return 'B'
        elif avg_grade > 70 and avg_grade < 80:
            return 'C'
        elif avg_grade > 60 and avg_grade < 70:
            return 'D'
        else:
            return 'F'
        
    
    def getgpa(self):
        """ Returns the GPA for the student

        Returns:
            float: The GPA for the student
        """

        gpa_dict = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        
        gpa = 0.0
        for grade in self.grades.values():
            letter_grade = self.toletter(grade)
            gpa += gpa_dict[letter_grade]

        return gpa / len(self.grades)
            

class Teacher:
    """
    A class representing a teacher
    
    Attributes:
      name (str): The name of the teacher.
      taughtclass (str): The class taught by the teacher
      students (list): The list of students in the class taught by the teacher

    """
    def __init__(self, name, taughtclass, file):
        """
        Initializes a Teacher object
        
        Args:
          name (str): The name of the teacher
          taughtclass (str): The class taught by the teacher
          file (str): The name of the json file containing the list of students in the class
        """
        self.students = []
        self.name = name
        self.taughtclass = taughtclass
        with open (file, "r") as f:
            data = json.load(f)
        
        for dicts in data:
            if (str(dicts) == self.taughtclass):
                for item in dicts:
                    self.students.append(dicts[item])
        
        
    def gradeassign(self, file):
        """
        Assigns grades for a given assignment to all students in the class. The method takes in a list of student objects 
        from the teacher's dictionary, and returns a new list containing the grades of each student for the following assignment.
        
        Args:
          file (str): The name of the json file containing the list of students in the class.
        
        Returns:
          grades (dict): A dictionary where the keys are the student names and the values are 
        their grades for the assignment
        """
        grades = {}
        for indiv in self.students:
            grade = indiv.grades[self.taughtclass]
            new_grade = grade + 2.5 if grade > 75 else grade - 2.5
            grades[indiv.name] = new_grade
        
        return grades
      
        
    def curveoverall(self, curvepercent, curve = "yes"):
        """
        Curves the grades of students in the class based on a given percentage.
        
        Args:
          curvepercent (float): The percentage by which to curve the grades.
          curve (str): A flag indicating whether or not to curve the grades. Default is "yes".
        
        Returns:
          newgrades (dict): A dictionary where the keys are the student names and the values are 
        their curved grades.
        """
        newgrades = {}
        for indiv in self.students:
            if curve == "yes":
                newgrades[indiv.name] = indiv.grades[self.taughtclass] + curvepercent
            else:
                newgrades[indiv.name] = indiv.grades[self.taughtclass]

        return newgrades
    
    
def main(Mainfile, Sidefile):
   # stud = Student(Mainfile, "Eyal")
    teach = Teacher("Mr. Kane", "Math", Mainfile)
    datab = SchoolDatabase("UMD", Sidefile)
    #should print a datframe based on the tempjsondict
    datab.df.head()
    
    print(f'Students in class: {teach.students}')
  

def parse_args(argslist):
  parser = ArgumentParser()
  parser.add_argument("Mainfile", help= "file of all classes,teachers,students.")
  parser.add_argument("Sidefile", help= "Will be reomved later")
  return parser.parse_args(argslist)


if __name__ == "__main__":
  args = parse_args(sys.argv[1:])
  main(args.Mainfile, args.Sidefile)