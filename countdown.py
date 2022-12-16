import time

print("Welcome to the countdown timer!")

# get the countdown duration from the user
duration = int(input("Enter the countdown duration in seconds: "))

# loop for the given duration
for i in range(duration, 0, -1):
  # print the current time remaining
  print(i)
  # pause for 1 second
  time.sleep(1)

# print a message when the countdown is complete
print("Time's up!")