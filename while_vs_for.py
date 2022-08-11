# while vs for
num = 1
res = 0
digit = 0
while num < 5:
    res += num
    num += 1
print(res)

for value in range(5):
    digit += value
print(digit)
