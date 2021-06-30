def main():
	s='this is a string'
	for c in s:
		if c=='s':
			continue
		print (c,end='')
	print (end='\n')

	for c in s:
		if c=='s':
			break
		print (c,end='')
	print (end='\n')
if __name__ == '__main__':
	main()