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
        
          
    
    
