class A:
    def feature1(self):
        print("inside feature 1")
    def feature2(self):
        print("inside feature 2")

class B(A):
    def feature3(self):
        print("inside feature3")
    def feature4(self):
        print("inside feature 4")

class c(B,A):
    def feature5(self):
        print("inside feature 5")

class D(c):
    def feature6(self):
        print("inside feature 6")

a=c()
