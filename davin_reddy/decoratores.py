#decoratores
@smart_div
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner1(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner1

div(2,5)
div1=smart_div(div)
# div=smart_div(div)

div1(2,5)