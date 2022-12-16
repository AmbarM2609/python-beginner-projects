# Define a function to check if a string is a palindrome
def is_palindrome(input_string):
    # Remove any non-alphanumeric characters and convert to lowercase
    clean_string = ''.join(c.lower() for c in input_string if c.isalnum())

    # Check if the string is a palindrome
    return clean_string == clean_string[::-1]

# Prompt the user for a string
input_string = input('Enter a string: ')

# Check if the string is a palindrome and print the result
if is_palindrome(input_string):
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')
