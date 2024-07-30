def fun():
    i=1
    while i<=200:
        yield i
        i=i+1
    return i

print(fun())
x=fun()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(list(x))
