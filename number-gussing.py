import random

print("Welcome to the guess the number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# generate a random number between 1 and 100
target = random.randint(1, 101)

# set the initial number of guesses to 0
guesses = 0

# loop until the player guesses the correct number
while True:
  # get the player's guess
  guess = int(input("Enter your guess: "))
  # increment the number of guesses
  guesses += 1
  # check if the guess is correct
  if guess == target:
    print(f"You guessed it in {guesses} guesses! Congratulations!")
    break
  # if the guess is too high or too low, print a hint
  elif guess > target:
    print("Too high. Try again.")
  else:
    print("Too low. Try again.")
