
class Animal():
	def __init__(self):
		print('I\'m Animal')
	def walk(self): print('Hey, Animal walk')
	def talk(self): print('Hey, Animal talk')

class Duck(Animal):
	def __init__(self):
		print('I\'m Duck')
		super().__init__()
	def walk(self): 
		print('Hey, Duck walk')
		super().walk()

def main():
	donald=Duck()
	donald.walk()
	donald.talk()

if __name__ == '__main__':
	main()