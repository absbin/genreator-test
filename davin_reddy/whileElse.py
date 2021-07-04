def main():
	s='this is a string'
	i=0
	while (i<len(s)):
		if s[i]=='s':
			print('\nif condition activated\n')
			break
		print(s[i],end='')
		i+=1
	i=0

	while (i<len(s)):
		print(s[i],end='')
		i+=1
	else:
		print('\nelse activated\n')

if __name__ == '__main__':
	main()