
a = 5
b = 0
b = 2
# k=int(input("Enter a Number : "))
try:

    print("Resources open")
    b = int(input("Enter a Number : "))
    print(a/b)
except ZeroDivisionError as e1:  # we know the Error
    print("Excepion occuered as ", e1)

except ValueError as e2:  # we know the Error
    print("Excepion occuered as ", e2)

except Exception as e2:  # we dont know the Error
    print("Excepion occuered as ", e2)
finally:
    print("Resourses close")
