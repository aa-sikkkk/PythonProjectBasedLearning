#Calculator Program.
#What features: 1.menu 2.input options 

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def division(a,b):
    if b != 0:
        return a/b
    else:
        print("Divison Error")
    
def rem(a,b):
    return a%b
def multi(a,b):
    return a*b

def menu():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Reminder")
    print("5.Multiply")
    print("6.Exit")

def main():
 while True:
        menu()
        choice = input("Enter choice (1/2/3/4/5/6): ")
        
        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4','5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {sub(num1, num2)}")

            elif choice == '3':
                print(f"{num1} / {num2} = {division(num1, num2)}")

            elif choice == '4':
                result = rem(num1, num2)
                print(f"{num1} % {num2} = {result}")
            elif choice == '5':
                print(f"{num1} * {num2} = {multi(num1,num2)}")
        else:
            print("Invalid choice. Please select a valid option.")
        
if __name__ == "__main__":
    main()
