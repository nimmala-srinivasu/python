secret_number = 7
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input('Guess number: '))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
    print("Wrong guess")
else:
    print("sorry,you failed")
