class A:
	def show():
		print('in class A')

class B(A):
	def show():
		print('in class B')

def main():
	o1=A()
	o2=B()
	o1.show
	o2.show


if __name__ == '__main__':
	main()
		