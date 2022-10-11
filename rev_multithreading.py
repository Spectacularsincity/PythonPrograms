from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(20):
            print("hello")
            sleep(1)

class Hai(Thread):
    def run(self):
        for i in range(20):
            print("Hai")
            sleep(1)


a=Hello()
b=Hai()
a.start()
sleep(0.2)
b.start()

a.join()
b.join()

print("bye")


# to make it print simultaneously we use thread
# here collision is happening so we have to do something
#ideally bye should print after hello and hai as here bye uses main thread not t1 nor t2 so use join.