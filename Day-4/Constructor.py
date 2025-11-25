class Student:
    def __init__(self, name, cgpa):
        # print("Constructor was called...")
        self.name = name
        self.cgpa = cgpa
        
    def get_cgpa(self):
        return self.cgpa
        
stu1 = Student("Rahul", 9.0)
stu2 = Student("Urvashi", 8.2)
stu3 = Student("Ahardha", 9.4)

print(stu1.name, "cgpa = " , stu1.cgpa)
print(stu2.name, "cgpa = ", stu2.cgpa)
print(stu3.name, "cgpa = " , stu3.cgpa)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")