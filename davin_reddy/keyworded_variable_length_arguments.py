# keyworded_variable_length_arguments.py


def person(name, **data):
    print(name)
    print(type(data), data)
    # or
    for i, j in data.items():
        print(i, j, end="     ")
    print()
    for i, j in data.items():
        print(i, j)


person("Abbas", age=35, city="Shiraz", phone=912080)
