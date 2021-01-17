from random import randint
num = randint(1,100)
guesses = [0]

print(" ")
print('Hello, welcome to the GUESS THE NUMBERS GAME')
print("Your task is to guess the number from 0 to 100")
print(" ")

while True:

    guess = int(input("\nI'm thinking of a number between 1 and 100.\nGuess a number? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    elif guess == num:
        print(f"CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!")
        break

    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')

    guesses.append(guess)

    break

while True:

    guess = int(input("\nI'm thinking of a number between 1 and 100.\nGuess a number? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    if guess == num:
        print(f"CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!")
        break

    guesses.append(guess)


    if abs(num - guess) < abs(num - guesses[-2]):
        print('WARMER!')
    else:
        print('COLDER!')