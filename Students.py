import json




#Will a teacher also have composition of a student? Most likely combine 
# teachers and students file into one when done.
class Student:
    #The following class is going to represent the student objects for the 
    #gradedatabase. 
    
    
    
    
    
    def __init__(self, file, name, info):
        #can update args to see what more to add.
        """
        
        
        
        """
        self.grades = {}
        self.classname = []
        self.name = name
        index = 0
        with open (file, "r") as f:
            data = json.load(f)
            for years in data:
              for dicts in years:
                  while (index < 3):
                    for items in dict:
                        if dict[items] == self.name:
                            self.grades[items] = items
                            self.classname.append(str(items))
                            
        
                  
    
    def __str__(self):
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
        
    
    def update_grade(self, year, subject, student_name, new_grade):
        """Updates the grade of a specific student for a given subject and year. The method first checks if the year 
        and subject provided exist in the grades dictionary, and if the student name is enrolled in that subject for 
        that year. If the student is found, the method updates their grade to the new value provided and sorts the grades 
        for that subject and year in ascending order.

        Args:
            year (int): The year of the grades to be updated
            subject (str): The subject of the grades to be updated
            student_name (str): The name of the student whose grade is to be updated
            new_grade (int): The new grade to assign to the student

        """
        if year in self.grades and subject in self.grades[year]:
            if student_name in self.grades[year][subject]:
                self.grades[year][subject][student_name] = new_grade
                sorted_grades = sorted(self.grades[year][subject].items(), key=lambda x: x[1])
                print(f"Updated {student_name}'s grade in {subject} for year {year} to {new_grade}")
                print(f"The sorted grades in {subject} for year {year} are: {sorted_grades}")
            else:
                print(f"{student_name} is not enrolled in {subject} for year {year}")
            
            
    def studying(self, hours, percent_inc = 0.0):
        # I dunno maybe make something that returns an increased possiblity
        # of what their grade will be for the teacher class.
        if hours > 0:
            percent_inc = hours/8
            for grades in self.grades:
                self.grades[grades] += percent_inc
        else:
            print("Student is Lazy")
        
    
    def dispgpa(self):
        # Will most likely make a new dictionary on the top transfer
        #letter grades to gpa.
        gpa = 0.0
        return gpa
        
          
    
    
class Teacher:
#Still some updates for the following teacher and student class to come. 
#After learning about pandas, I want to make the overall Grade_Database file
#implement both the student as well as teacher class, that way it can process
# all the information and create a database with students, classes taken, teachers for classes,
#and grades all in a single database.
#final design for grade_database will also include filtered panda structures 
#defining honor roll students, etc.    
    
#Still a couple more functions to define for teacher class, and still needs to define student class.
    def __init__(self, name, students, taughtclass, file):
        self.students = []
        self.name = name
        self.taughtclass = taughtclass
        with open (file, "r") as f:
            data = json.load(f)
        
        for dicts in data:
            if (dicts == self.taughtclass):
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
