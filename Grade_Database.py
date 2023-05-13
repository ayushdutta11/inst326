from argparse import ArgumentParser
import json
import pandas as pd
import sys
import re 

# For all of the docstrings, there is still some info missing.
# What to add: Contributer of method, techniques displayed
class SchoolDatabase:
    "A data collection that sort outs and grades peoples homework"

    "These are my first commits"

    def __init__(self, schoolname, file, classes = None, gpas = None):
      self.schoolname = schoolname
      #rep the classes alongside with how teaches it for the dataframe
      #will change tempsjondict to make it so the dictionaries are nested
      #so that the datframe can also have a class name column

      with open (file, "r") as f:
            data = json.load(f)
            self.df = pd.DataFrame.from_dict(data, orient = "index")
            
            
      #gpas reps all of the gpa's of students
      #Converting all the info into json file into dataframe

    
    def similarclasses(self):
      #using for sets
      pass
  
    def honor_roll(self):
      #Will define a lmabda/list comprhension of students with above 3.0's.
      pass
    
    
    def classes_by_year(self):
      #Define two different data plots using dataframes, will display 
      pass
  


#Will a teacher also have composition of a student? Most likely combine 
# teachers and students file into one when done.
class Student:
    """ The following represents a student. The following student 
    will have components representing information about their school,
    alongside with their grades. Will be used in order to retrieve
    information about student in the SchoolDatabase class.
    
    Attributes:
      name (str)
      grades (dict)
      classname ()
    """
    
    
    
    
    
    def __init__(self, file, name):
        #can update args to see what more to add.
        """
        Initializes a student object.
        
        Args: 
            file (str): filepath to the gradesdict.json file
            name (str): student name 
        Side effects:
            self.grades, self.classname, and self.name get populated by their 
            corresponding values.
        """
        #text file will be potentially used to populate student info attribute section.
        self.grades = {}
        self.classname = []
        self.name = name
        index = 0
        with open (file, "r") as f:
            data = json.load(f)
            for year, schoolinfo in data.items():
              for key, items in schoolinfo.items():
                  if re.search(r"^[a-z]", key):
                    for student, grade in items.items():
                        if student == self.name:
                            self.grades[key] = int(grade)
                            self.classname.append(key)

                           
        
                  
    
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
        
        
    def toletter(self, grade):
        '''
        Converts numerical grade to letter name

        Args:
            grade (int): numerical grade in course
        Returns:
            str: corresponding letter grade 
        '''
            #combine with __displaygrades__
        return ('A' if 90 <= grade <= 100 else 
                'B' if 80 <= grade < 90 else 
                'C' if 70 <= grade < 80 else
                'D' if 60 <= grade < 70 else 
                'F'
                )

        
            
    def studying(self, hours, percent_inc = 0.0):
        # I dunno maybe make something that returns an increased possiblity
        # of what their grade will be for the teacher class.
        if hours > 0:
            percent_inc = hours/8
            for grades in self.grades:
                self.grades[grades] += percent_inc
        else:
            print("Student is Lazy")
        
    
    def getgpa(self):
        # Will most likely make a new dictionary on the top transfer
        #letter grades to gpa.
        gpa = 0.0
        for classes in self.grades:
            #if (grade == A):
              gpa += 4
              
              
              
        gpa / len(self.grades)
            
            
          
          
        
          
    

class Teacher:
#Still some updates for the following teacher and student class to come. 
#After learning about pandas, I want to make the overall Grade_Database file
#implement both the student as well as teacher class, that way it can process
# all the information and create a database with students, classes taken, teachers for classes,
#and grades all in a single database.
#final design for grade_database will also include filtered panda structures 
#defining honor roll students, etc.    
    
#Still a couple more functions to define for teacher class, and still needs to define student class.
    def __init__(self, name, taughtclass, file):
        self.students = []
        self.name = name
        self.taughtclass = taughtclass
        with open (file, "r") as f:
            data = json.load(f)
        
        for dicts in data:
            if (str(dicts) == self.taughtclass):
                for item in dicts:
                    self.students.append(dicts[item])
                    
        #have to iterate through some sort of file to append students to
        #the teachers students attribute.
        
        
    
    def gradeassign(self, file):
        #The following method will take in a the list of student objects from the
        #teacher's dictionary, and return a new list containing the grades of 
        #each student for the following assignment. 
        #Will be useful for constructing column of dataframe which contains all assignments alongside with grades.
         grades = {}
         for indiv in self.students:
             grade = self.students[indiv]
             new_grade = grade + 2.5 if grade > 75 else grade - 2.5
             grades[indiv] = new_grade
        
         return grades
      

        
        
    def curveoverall(self, curvepercent, curve = "yes"):
        #The final will decide whether or not the teacher decides to curve the grades of the students,
        # and the increase will be given by the curvepercent arg.
        newgrades = {}
        for indiv in self.students:
            if curve == "yes":
             for indiv in self.students:
                 newgrades[indiv] = self.students[indiv] + curvepercent
            else:
                newgrades[indiv] = self.students[indiv]

        return newgrades
    
    
def main(Mainfile, Sidefile):
   # stud = Student(Mainfile, "Eyal")
    teach = Teacher("Mr. Kane", "Math", Mainfile)
    datab = SchoolDatabase("UMD", Sidefile)
    #should print a datframe based on the tempjsondict
    datab.df.head()
    
    print(f'{teach.students}')
  

 

def parse_args(argslist):
  parser = ArgumentParser()
  parser.add_argument("Mainfile", help= "file of all classes,teachers,students.")
  parser.add_argument("Sidefile", help= "Will be reomved later")
  return parser.parse_args(argslist)


if __name__ == "__main__":
  args = parse_args(sys.argv[1:])
  main(args.Mainfile, args.Sidefile)