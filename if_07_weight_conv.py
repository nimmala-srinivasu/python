weight = float(input('Enter Weight: '))
unit = input("""Enter units of weight
pounds - L 
Kilograms - K
""")
if unit.upper() == "L":
    convert = weight * 0.45
    if 60 <= convert <= 90:
        print(f'you are {convert} KG and Healthy')
    else:
        print(f'you are {convert} KG and Eat healthy food')
else:
    convert = weight / 0.45
    if 133.33 <= convert <= 200:
        print(f'you are {convert} Lbs and Healthy')
    else:
        print(f'you are {convert} Lbs and Eat healthy food')
