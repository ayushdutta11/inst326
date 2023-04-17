class Student:
    """Represents the student
    
    Attributes:
        name (str) = Name of the student
        student_id (int) = The ID of the student
        classes (dict) = A nested dictionary containing classes as keys 
        and assignments with their grades as values
    
    """
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.classes = {}
        
    def display_graddes(self, min_grade=None):
        """Displays the student's grades for each assignment
        
        Args:
            min_grade (int, optional): The minimum grade to display
        """
        for class_name, assignments in self.classes.items():
            print(f"{class_name}")
            for assignment_name, grade in assignments.items():
                if min_grade is None or grade >= min_grade:
                    print(f"{assignment_name}: {grade}")