class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self,name):
        self.students.append(name)

    def count_students(self):
        return len(self.students)
    
cl = Classroom()
cl.add_student("hend")
print(f"The number of students in the class is : {cl.count_students()}")
cl.add_student("mohamed")
cl.add_student("jana")
print(f"The number of students in the class is : {cl.count_students()}")