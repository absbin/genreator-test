# decoratores


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


@smart_div
def div(a, b):
    print(a / b)


div(2, 5)
div(5, 2)


@smart_div
def sorted(a, b):
    print(a, b)


sorted(5, 6)
sorted(6, 5)
smart_div(div(1, 2))
smart_div(div(2, 1))
