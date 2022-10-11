class Car:
    wheels=4

    def __init__(self):
        self.milage=10
        self.company='BMW'


c1=Car()
c2=Car()


c1.milage=20


Car.wheels=5
c1.wheels=10
c2.wheels=20

print(Car.wheels)

print(c1.milage,c1.company ,c1.wheels)
print(c2.milage,c2.company,c2.wheels)
