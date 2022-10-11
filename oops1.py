class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def congif(self):
        print("the config is: ", self.cpu,self.ram)


comp1=Computer('i5',16)
comp2=Computer('Ryzen 3',8)

comp1.congif()
comp2.congif()

