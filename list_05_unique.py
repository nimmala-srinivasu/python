numbers = [2, 2, 3, 5, 6, 8, 8, 9]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
