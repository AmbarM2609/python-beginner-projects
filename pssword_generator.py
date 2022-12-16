import random

# Define a function to generate a password
def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_characters):
    # Create a string of allowed characters
    allowed_characters = ''
    if include_uppercase:
        allowed_characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if include_lowercase:
        allowed_characters += 'abcdefghijklmnopqrstuvwxyz'
    if include_numbers:
        allowed_characters += '0123456789'
    if include_special_characters:
        allowed_characters += '!@#$%^&*()_+-=[]{};:\'",.<>?/\\|`~'

    # Generate the password
    password = ''
    for i in range(length):
        password += random.choice(allowed_characters)

    # Return the password
    return password

# prompts user for the password length and character options
length = int(input('Enter the password length: '))
include_uppercase = input('Include uppercase letters (y/n)? ') == 'y'
include_lowercase = input('Include lowercase letters (y/n)? ') == 'y'
include_numbers = input('Include numbers (y/n)? ') == 'y'
include_special_characters = input('Include special characters (y/n)? ') == 'y'

# Generate the password and print it to the screen
password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_characters)
print('Your password is:', password)