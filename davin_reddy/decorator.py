import time
def time_it(func):
    def wrapper(*arg,**kwargs):
        start=time.time()
        result=func(*arg,**kwargs)
        end=time.time()
        print(func.__name__,'took',(end-start)*1000, 'mil sec')
        return result
    return wrapper

@time_it  
def calc_square(numbers):
    result=[]
    for num in numbers:
        result.append(num*num)
    return result

@time_it
def calc_cube(numbers):
    result=[]
    for num in numbers:
        result.append(num*num*num)
    return result

array=range(1,100000)
calc_square(array)
calc_cube(array)