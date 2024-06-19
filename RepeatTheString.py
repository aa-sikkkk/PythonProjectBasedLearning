# PROGRAM THAT REPEATS EACH CHARACTER IN A STRING

# Define the function to double each character in the input string
def double(inputString):
    # Use a list comprehension to create a new string with each character doubled
    doubled = ''.join(char * 2 for char in inputString)
    return doubled

# Prompt the user to input a string
inputString = input("Type Anything: ")

# Call the double function with the input string and print the result
print(double(inputString))
