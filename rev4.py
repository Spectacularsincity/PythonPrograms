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

    def classmethods(cls):
        print(cls.school)

    @staticmethod

    def values():
        print("inside static method")

c1=Student(77,89,90)
c2=Student(89,99,90)

print(c1.Average())
print(c2.Average())

c1.classmethods()
c2.classmethods()

c1.values()
c2.values()

Student.values()
Student.classmethods()


