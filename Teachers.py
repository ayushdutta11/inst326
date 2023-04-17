import json

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
    