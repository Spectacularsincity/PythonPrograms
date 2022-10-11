class A:
    def show(self):
        print("in A's Show")

class B(A):
    def shows(self):
        print("in B's show")

a=B()
a.show()
