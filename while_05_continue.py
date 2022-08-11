var = 3
while var > 0:
    print(var)
    var -= 1
    if var == 1:
        continue
        print("Still in IF block")
    print("Still in WHILE loop")
print("Out of WHILE loop")
