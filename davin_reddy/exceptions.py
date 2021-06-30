def main():
	try:
		for line in readfile('Ghaznavi.txt'): print(line)
	except IOError as e:
		print('Could nt open the file : ' ,e)
	except ValueError as e:
		print('Bad filename: ', e)

def readfile(filename):
	if filename.endswith('.txt'):
		fh=open(filename)
		return fh.readlines()
	else:
		raise ValueError ('Wrong file extention')

if __name__ == '__main__':
	main()


