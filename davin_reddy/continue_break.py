def main():
	s="this is a string"

	for c in s:
		if c=='s':break
		print(c,end='')
	print("\n********")
	for c in s:
		if c=='s':continue
		print(c,end='')
	print("\n********")

if __name__=="__main__":main()
