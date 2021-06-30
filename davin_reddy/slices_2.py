def main():
	list1=list(range(1,100))
	print(type(list1))
	list1[27:43:5]=(500,500,500,500)
	print('list1 slice: ',list1[27:43])

if __name__ == '__main__':
	main()
