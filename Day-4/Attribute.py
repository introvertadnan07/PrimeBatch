class Student:
    college_name = "IIT Delhi" # class
    
    def __init__(self, name, gpa):
        self.name = name #instance
        self.gpa = gpa
        
stu1 = Student("Anum", 9.7)
print(stu1.name)
print(Student.college_name)
        