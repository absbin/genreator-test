# from threading import Thread

results=[]

def cal_square(numbers):
    # global results
    for i  in numbers:
        print("square:"+ str(i*i))
        results.append(i*i)        
    print("results square:", results)

def cal_cube(numbers):
    for i  in numbers:
        print("cube:",i*i*i)
        results.append(i*i*i)
    print("results cube:", results)
    
if __name__ == "__main__":
    arr=[2,3,4]   
    p1=cal_square(arr)
    p2=cal_cube(arr)
  
    print("Done!")
    print("results: ",results)
#print("results square2:", results)            
