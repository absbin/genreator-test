
class Duck:
	def  __init__(self,color='white',**kwargs):
		self._color=color
		self.variables={}
	def set_color(self,color,**kwargs):
		self._color=color
		self.variables=kwargs
	def get_color(self):
		return self._color,self.variables

def main():
	donald=Duck()
	print (donald.get_color())
	donald.set_color('green',feathers='white',beak='orange',feets='orange')
	print (donald.get_color())

if __name__ == '__main__':
	main()