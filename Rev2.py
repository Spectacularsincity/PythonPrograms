class Computer:
    def __init__(self):
        self.name="Sidharth"
        self.age=26

    def update(self):
        self.age=50

    def compare(self,other):
        if self.age==other.age:
            print("they are same")
        else:
            print("they are different")

c1=Computer()
c2=Computer()

c2.update()

print(c1.compare(c2))

