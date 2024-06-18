# Function definition to check if a number is Armstrong or not
def arm():
    num = int(input("Enter a number: "))  # Take user input for the number to check
    result = 0  # Initialize a variable to store the sum of powers of digits
    original = num  # Store the original input number in a variable
    n = len(str(original))  # Calculate the number of digits in the original number
    
    # Loop to calculate sum of nth power of each digit
    while num != 0:
        rem = num % 10  # Extract the last digit of num
        result = result + rem ** n  # Add nth power of the digit to result
        num = num // 10  # Remove the last digit from num
    
    # Check if the original number is equal to the calculated result
    if original == result:
        print(f"The number {original} is an Armstrong number.")  # Print if number is Armstrong
    else:
        print(f"No, the number {original} is not an Armstrong number.")  # Print if number is not Armstrong

# Call the function to execute the program
arm()
