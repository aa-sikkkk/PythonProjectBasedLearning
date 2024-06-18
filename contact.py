#Contact Management System

contacts = {}
def menu():
    print("\n Contact Management System Menu:")
    print("1. Add a new contact")
    print("2. Delete a contact")
    print("3. Update a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit")

def addContact():
    name = input("Enter Name of the contact: ")
    phone = input("Enter phone of the contact: ")
    email = input("Enter email of the contact: ")
    contacts[name] = {'phone' : phone, 'email' : email}
    print(f"Succcessfully added {name} as contact")

def delContact():
    name = input("Enter the name of the contact for deletion: ")
    if name in contacts:
        del contacts[name]
        print(f"Succcessfully deleted {name} from contact")
    else:
        print("Contact Not Found")

def upContact():
    name = input("Enter the name of the contact to Update: ")
    if name in contacts:
       phone = input("Enter new number for the contact(Leave this empty for current): ")
       email = input("Enter new email for the contact(Leave this empty for current): ")
       if phone:
            contacts[name]['phone'] = phone
       if email:
            contacts[name]['email'] = email   
       print("Succcessfully updated the Contact from contact")
    else:
        print(f"Contact {name} not found")

def searchContact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Contact {name} found")
        print(f"phone: {contacts[name]['phone']} ")
        print(f"email: {contacts[name]['email']} ")
    else:
        print("Contact Not Found")

def displayContact():
    print("Displaying all the Contacts")
    if contacts:
        for name in contacts:
            print(f"name: {name} phone: {contacts[name]['phone']} email: {contacts[name]['email']}")
    else:
        print("Contact Not Found in the list")

def main():
    while True:
        menu()
        choice = input("Enter number (1-6): ")
        if choice == '1':
            addContact()
        if choice == '2':
           delContact()
        if choice == '3':
            upContact()
        if choice == '4':
            searchContact()
        if choice == '5':
            displayContact()
        if choice == '6':
            print("Exiting the Contact Management System")
            break
if __name__ == "__main__":
    main()

        
