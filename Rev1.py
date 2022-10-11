class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def configure(self):
        print("the configuration is : " + self.cpu, self.ram)

c1=Computer('I5','8GB')
c2=Computer('I7','16GB')

c1.configure()
c2.configure()
