class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name)
        print(self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand='HP'
            self.cpu="I5"
            self.Ram=8

        def show(self):
            print(self.brand,self.cpu,self.Ram)


s1=Student("jenny",25)
s2=Student("Sid",26)

s1.show()
s2.show()



lap1=s1.lap
lap2=s2.lap

lap3=Student.Laptop()

print(lap1.brand)
print(lap2.cpu)
print(lap3.Ram)

s1.show()