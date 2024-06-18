#Python Program to Check wheather a number and string is palindrome or not!

#Reverse and check the string
def string(inputString):
    reverseString = inputString[::-1]

    if inputString == reverseString:
        return True
    else: 
        return False

#Reverse and Check the Number
def checkPalNUM(a):
    original = a
    reverse = 0
    
    while a != 0:
        rem = a % 10
        reverse = reverse * 10 + rem
        a = a // 10

    if original == reverse:
        return True
    else: 
        return False
    
def menu():
    print("WELCOME TO PALINDROME CHECKER\n")
    print("1. TO CHECK NUMBER")
    print("2. TO CHECK STRING")
    print("3. EXIT")

def main():
    while True:
        menu()
        choice = input("Enter the number 1-3: ")
        if choice == '3':
            print("Exiting the program...")
            break
        
        elif choice == '1':
            a = int(input("Enter the number to check: "))
            if checkPalNUM(a):
                print("The given number is a palindrome\n")
            else:
                print("The given number is not a palindrome\n")
        
        elif choice == '2':
            inputString = input("Enter the string to check: ")
            if string(inputString):
                print("The given string is a palindrome\n")
            else:
                print("The given string is not a palindrome\n")
        
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


