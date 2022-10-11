class Student:
    def __init__(self):
        self.name='Sidharth VK'
        self.age=26
        self.lap=self.Laptop()

    def show(self):
        print(self.name)
        print(self.age)
        self.lap.shows()

    class Laptop:
        def __init__(self):
            self.com="HP"
            self.model="Ryzen"

        def shows(self):
            print(self.com)
            print(self.model)

s1=Student()
s2=Student()

s1.show()
s2.show()

lap1=s1.lap
lap2=s2.lap

print(lap2.com)
print(lap1.com)

lap1.shows()
lap2.shows()

lap3=Student.Laptop
lap3.shows()


