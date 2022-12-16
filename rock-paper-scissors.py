import random

def play_rock_paper_scissors():
  # display a message to the user to make a choice
  print("Make your choice: rock, paper, or scissors")
  
  # get the user's choice
  user_choice = input()
  
  # create a list of possible choices for the computer
  computer_choices = ["rock", "paper", "scissors"]
  
  # have the computer choose a random option from the list of possible choices
  computer_choice = random.choice(computer_choices)
  
  # compare the user's choice to the computer's choice
  # and determine the winner
  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
  elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
  elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
  else:
    print("The computer wins!")

# start the game
play_rock_paper_scissors()
