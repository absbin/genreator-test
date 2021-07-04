def counter(num):
    print("Function Starting")
    for i in range(3):
        print('Before Yield',end=" ,")
        yield num
         
        num=num+1
        print('After Yield')

cnt=counter(3)
try:
	print(next(cnt),end=", ")
	print(next(cnt),end=", ")
	print(next(cnt),end=", ")
	print(next(cnt),end=", ")
except:
	raise StopIteration


print('Done')
