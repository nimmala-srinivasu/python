numbers = [4, 8, 14, 25, 0, 3, 37, 14, 1]
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print('Maximum number is ', maximum)
print("And it's index ", numbers.index(maximum))
