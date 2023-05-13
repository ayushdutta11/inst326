import Grade_Database as gd

def main(file, name):
    '''
    #Docstring
    '''

    student = gd.Student(file, name) 
    print(student.name)
    for course in student.classname:
        grade = student.grades[course]
        print(course, grade, student.toletter(grade))

if __name__ == "__main__":
    main("gradesdict.json", "Simon")


