from datetime import datetime
number_of_lines=20
f=open('Ghaznavi.txt','r')
chunk=f.read(number_of_lines)
f.close()
print(chunk)


im=open('Koala.jpg','rb')
filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
im2=open(filename1 +'.jpg','wb')


buffersize=50000
buffer=im.read(buffersize)
while len(buffer):
	im2.write(buffer)
	print('50k',end='')
	buffer=im.read(buffersize)
print('done')
