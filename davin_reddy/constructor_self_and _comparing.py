class Computer:
    def __init__(self):
        self.name = "abbas"
        self.age = 35

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
print(c1.name,c1.age)
print(c2.name,c2.age)
c2.update()
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
