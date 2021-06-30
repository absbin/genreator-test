import re
import os

print(__file__)
print(__name__)
print(os.path.basename(__file__))
print('Hello World!')

def main():
	fh=open('Ghaznavi.txt')
	for line in fh:
		if re.search('(theses | thesis)',line):
			print(line)

if __name__ == '__main__':
	main()