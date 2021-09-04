class Student:
    
    univ = "penn"
    def __init__(self,name,dept):
        self.student_name = name
        self.student_dept = dept
    
    def print_all(self):
        print("name: " + self.student_name)
        print("dept: " + self.student_dept)

student1 = Student("mike", "cis")
student1.print_all()
Student.print_all(student1)

class AI_student(Student):
    def __init__(self,name,dept):
        Student.__init__(self,name,dept)

student2 = AI_student("H", "Cit")
student2.print_all()