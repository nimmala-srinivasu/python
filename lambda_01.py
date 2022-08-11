def myfunc(n):
    return lambda a: a * n


myDoubler = myfunc(2)
myTripler = myfunc(3)

print(myDoubler(11))
print(myTripler(11))
