# class Student:
#     def __init__(self,python,web,math):
#         self.subject1=python
#         self.subject2=web
#         self.subject3=math
#     def avgcal(self):
#         return (self.subject1+self.subject2+self.subject3)/ 3
# student1=Student(1,4,9)
# student2=Student(45,87,89)
# print(student1.avgcal())
# print( student2.avgcal())
class Student:
    collegename="LPU"
    def _init_(self, python, web,math):
        self.subject1 = python
        self.subject2 = web
        self.subject3 = math
    def avgcal(self):
        return(self.subject1 + self.subject2 + self.subject3)/3
    # def get_subject1(self):
    #     return self.subject1
    # def set_marks(self,value):
    #     self.subject1=value
#BELOW IS CLASS METHOD
    @classmethod
    def collegedetails(cls):
        return cls.collegename
student1 = Student(90, 80, 95)
student2 = Student(100, 85, 70)
print(student1.avgcal())

print(Student.collegedeatils())
