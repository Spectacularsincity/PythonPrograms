class Car:
    wheels=10

    def __init__(self):
        self.carname="Merceded Benz"
        self.milage="50 miles"

c1=Car()
c2=Car()

print(c1.milage)
print(c1.carname)

Car.wheels=50
c1.wheels=20
c2.wheels=30

print(Car.wheels)

print(c1.wheels,c1.milage,c1.carname)
print(c2.wheels,c2.milage,c2.carname)
