
def main():
	testfunc(1,2,3,4,5,6,7,8,9)
	kwargsFunc(one=1,two=2,three=3)
	argsKwargs(0,1,2,3,four=4,five=5)

def testfunc(this , that, other,*args):
	print(this,that,other,*args, end=',')
	print('\n',this,that,other,args,'\n', end=',')

def kwargsFunc(**kwargs):
	print(kwargs)
	print(*kwargs,'\n',end=',')

def argsKwargs(this,that,*args,**kwargs):
	print(this,that,args,kwargs)
	print(this,that,*args,*kwargs)


if __name__ == '__main__':
	main()