
import sys
i=0
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
def greet():
    global i
    i+=1
    print("Hello",i)
    greet()

greet()

