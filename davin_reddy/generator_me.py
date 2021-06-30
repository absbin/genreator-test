def counter(num):
    print("Function Starting")
    for i in range(5):
        print('Before Yield')
        yield num
        num=num+1
        print('After Yield')

cnt=counter(3)
print('cnt type is:',type(cnt))

print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))
# print(next(cnt))
print('Done')
