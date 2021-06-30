class Student:
	def sum(a=None,b=None,c=None, *args):
		if a!=None and b!= None and c!=None and args!=None:
			return a+b+c+sum(args)
		elif a!=None and b!= None and c!=None:
			return a+b+c
		elif a!=None and b!=None:
			return a+b
		else :
			return a

def main():
	s1=Student

	print(s1.sum(1,2,3,4,))
	print(s1.sum(1,2,3))
	print(s1.sum(1,2))
	print(s1.sum(1))

if __name__ == '__main__':
	main()
