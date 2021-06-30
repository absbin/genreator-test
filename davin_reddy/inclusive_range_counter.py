
class InclusiceRange:
	def __init__(self, *args):
		numargs=len(args)
		if numargs==0:raise TypeError('Reuire at least one number')
		elif numargs==1:
			self.start=1
			self.stop=args[0]
			self.step=1

		elif numargs==2:
			(self.start,self.stop)=args
			self.step=1

		elif numargs==3:
			(self.start,self.stop,self.step)=args

		else: raise TypeError('InclusiceRange expected at most 3 argument,got {}'.format(numargs))

	def __iter__(self):
		i=self.start
		while i<=self.stop:
			yield i		
			i=i+self.step

def main():
	cnt=InclusiceRange(2)
	# cnt=InclusiceRange(2,10)
	# cnt=InclusiceRange(2,10,3)
	# cnt=InclusiceRange(2,10,3,2)
	for i in cnt:
		print(i,end=', ')

if __name__ == '__main__':
	main()