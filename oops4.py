class Student:

    school='Telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def Average(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value

    @classmethod
    def info(cls):
        return cls.school
    def getschool(cls):
        return cls.school

    @staticmethod
    def infos():
        print("this is student class ... ")

s1=Student(34,67,78)
s2=Student(88,98,90)
print(s1.Average())
print(s2.Average())

print(s1.info())
print(Student.info())

print(Student.infos())
