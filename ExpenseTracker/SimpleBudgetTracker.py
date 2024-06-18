import sqlite3

connect = sqlite3.connect('database.db')
curs = connect.cursor()

curs.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        date TEXT,
        category TEXT,
        amount REAL,
        type TEXT
    )
 ''')

connect.commit()
connect.close()

def add(date, category, amount, type):
    connect = sqlite3.connect('database.db')
    curs = connect.cursor()
    curs.execute('''
    INSERT INTO transactions (date, category, amount, type)
    VALUES (?, ?, ?, ?)
    ''', (date, category, amount, type))
    connect.commit()
    connect.close()

def view():
    connect = sqlite3.connect('database.db')
    curs = connect.cursor()
    curs.execute('SELECT * FROM transactions')
    rows = curs.fetchall()
    connect.close()
    return rows

def delete(transaction_id):
    connect = sqlite3.connect('database.db')
    curs = connect.cursor()
    curs.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
    connect.commit()
    connect.close()

def delete(transaction_id):
    connect = sqlite3.connect('database.db')
    curs = connect.cursor()
    curs.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
    connect.commit()
    connect.close()

def main():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            type = input("Enter type (income/expense): ")
            add(date, category, amount, type)
            print("Transaction added successfully!")
        
        elif choice == '2':
            transactions = view()
            for row in transactions:
                print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: {row[3]}, Type: {row[4]}")
        
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete(transaction_id)
            print("Transaction deleted successfully!")
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
