def topTen():
    yield 1
    yield 2
    yield 3
    yield 4

o1=topTen()
for i in o1:
    print(i)

def topTen2():
    n=1
    while(n<10):
        sq=n*n
        yield sq
        n+=1
o2=topTen2()
for i in o2:
    print(i)