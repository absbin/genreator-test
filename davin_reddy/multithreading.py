
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello",end=" , ")
            sleep(.2)
        print()

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi",end=" ,    ")
        print()
t1=Hello()
t2=Hi()
t1.run()
sleep(0.0020)#Because of collision between two threades
t2.run()
print("*************")
t1.start()
t2.start()
t1.join()
t2.join()
print("Bye")