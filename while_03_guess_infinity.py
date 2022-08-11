a = False
while not a:
    b = int(input("number: "))
    if b == 99:
        a = True
    else:
        print(b, "is not a correct guess")
print(b, "is a correct guess")
