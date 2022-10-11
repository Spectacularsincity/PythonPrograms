class Computer:
    def __init__(self):
        self.name='Sid'
        self.age=28

    def update(self):
        self.age=50

    def Compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1=Computer()
c2=Computer()
c1.update()

if c1.Compare(c2):
    print("they are same")
else:
    print("they are different")


print(c1.name)
print(c2.name)

