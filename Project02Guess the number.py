import random
num = random.randint(1, 12)

playerName = input("Hi! What's your name?")
numberOfGuesses = 0
print("Alright! " + playerName + " I am thinking of a number between 1 and 12:")

while numberOfGuesses < 7:
    guess = int(input())
    numberOfGuesses += 1
    if guess < num:
        print("Too low")
    if guess > num:
        print("Too high")
    if guess == num:
        break
if guess == num:
    print("You guessed it in " + str(numberOfGuesses) + "tries!" )
else:
    print ("Too bad, you did not guess the number, The number was " + str(num))




