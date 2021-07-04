feets=2
wheats=50
class Duck:	
	feets=3
	wheats=49
	def __init__(self,value1=0,value2=1):
		self._v1=value1
		self._v2=value2

	def _quack(self):
		print('Quaaack',self._v1,self._v2)
	
	@staticmethod
	def walking():
		print('walking: ',feets)
	
	def walking2():
		print('walking2',feets)
	
	@classmethod
	def eating(cls):
		wheats=51
		print('eating',wheats)

def main():
	donald=Duck(11,22)
	donald._quack()
	donald.walking()

	donald.eating()

	Duck.walking()
	Duck.walking2()
	wheats=52
	Duck.eating()



if __name__ == '__main__':
	main()
