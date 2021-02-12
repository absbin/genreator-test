
class  Student:

    def __init__(self,name,rollnu):
        self.name=name
        self.rollnu=rollnu
         

    def show(self):
        print(self.name,self.rollnu)

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student("Abbas",1)
s2=Student("Navin",2)

print(s1.name,s2.rollnu,"payan\n",end=' *-')
s2.show()
s2.lap.show()
s2.lap.cpu='i7'
s2.lap.ram=16
s2.lap.show()

    