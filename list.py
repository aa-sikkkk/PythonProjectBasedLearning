def listR(mixedList):
    # Filter out only integers from the mixedList
    IntegersOnly = [item for item in mixedList if isinstance(item, int)]
    return IntegersOnly

# Prompt user to input the number of items to put in the list
number = int(input("Enter the number of items to put in the list: "))

# Initialize an empty list to store mixed items
mixedList = []

# Loop to collect items from user input
for i in range(number):
    # Prompt user to enter an item for the list
    item = input(f"Enter item {i+1}: ")
    
    try:
        # Attempt to convert the input to an integer
        item = int(item)
    except ValueError:
        # If conversion fails, keep the item as a string
        pass
    
    # Add the item to the mixedList
    mixedList.append(item)

# Sort the mixedList in place
mixedList.sort()

# Call the listR function to filter integers from sorted mixedList
result = listR(mixedList)

# Print the resulting list containing only integers
print(result)
