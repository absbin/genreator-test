

class Pycharm:
    def execute(self):
        print("compling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Conversion check")
        print("compling")
        print("Running")

class Labtop:
    def code(self,ide):
        self.ide=ide.execute()
lap1=Labtop()

ide=Pycharm()
lap1.code(ide)
print("*************")
ide=MyEditor()
lap1.code(ide)
print("**************************")
ide.execute()