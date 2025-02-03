import mysql.connector

# Database Connection Function
def get_connection():
    try:
        return mysql.connector.connect(
            host='localhost', user='root',
            password='', database='HR'
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()

# Fetch All Employee IDs
def get_employee_ids():
    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute("SELECT id_emp FROM personel;")
            return {row[0] for row in curs.fetchall()}

# Register New Employee
def register():
    while True:
        idlist = get_employee_ids()
        try:
            id_emp = int(input('Enter employee ID: '))
        except ValueError:
            print("Invalid input! Please enter a numeric ID.")
            continue

        if id_emp in idlist:
            print("This Employee ID already exists. Try another!\n")
        else:
            name = input('Name: ')
            email = input('Email: ')
            phone = input('Phone Number: ')
            address = input('Address: ')
            salary = input('Salary: ')
            
            with get_connection() as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        "INSERT INTO personel VALUES (%s, %s, %s, %s, %s, %s);",
                        (id_emp, name, email, phone, address, salary)
                    )
                    conn.commit()
            print('EMPLOYEE SUCCESSFULLY REGISTERED!\n')
        
        if input('Register another employee? (Y/N): ').strip().upper() != 'Y':
            break

# View Employee Data
def view():
    try:
        id_emp = int(input('Enter Employee ID: '))
    except ValueError:
        print("Invalid input! Please enter a numeric ID.")
        return
    
    idlist = get_employee_ids()
    if id_emp not in idlist:
        print("Employee not found!\n")
        return

    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM personel WHERE id_emp = %s;", (id_emp,))
            for row in curs.fetchall():
                print(row)

# Update Employee Data
def edit():
    try:
        id_emp = int(input('Enter Employee ID: '))
    except ValueError:
        print("Invalid input! Please enter a numeric ID.")
        return
    
    if id_emp not in get_employee_ids():
        print("Employee not found!\n")
        return

    name = input('Name: ')
    email = input('Email: ')
    phone = input('Phone Number: ')
    address = input('Address: ')
    salary = input('Salary: ')
    
    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute(
                "UPDATE personel SET name=%s, email=%s, phone=%s, address=%s, salary=%s WHERE id_emp=%s;",
                (name, email, phone, address, salary, id_emp)
            )
            conn.commit()
    print("EMPLOYEE SUCCESSFULLY UPDATED!\n")

# Promote Employee
def promote():
    try:
        id_emp = int(input('Enter Employee ID: '))
    except ValueError:
        print("Invalid input! Please enter a numeric ID.")
        return

    if id_emp not in get_employee_ids():
        print("Employee not found!\n")
        return

    salary = input('New Salary: ')
    
    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute("UPDATE personel SET salary=%s WHERE id_emp=%s;", (salary, id_emp))
            conn.commit()
    print("EMPLOYEE SUCCESSFULLY PROMOTED!\n")

# Delete Employee
def delete():
    try:
        id_emp = int(input('Enter Employee ID: '))
    except ValueError:
        print("Invalid input! Please enter a numeric ID.")
        return

    if id_emp not in get_employee_ids():
        print("Employee not found!\n")
        return
    
    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute("DELETE FROM personel WHERE id_emp = %s;", (id_emp,))
            conn.commit()
    print("EMPLOYEE SUCCESSFULLY DELETED!\n")

# Main Menu
def main():
    while True:
        print('\n***** HR MANAGEMENT *****')
        print('1. Register Employee')
        print('2. View Employee Data')
        print('3. Edit Employee Data')
        print('4. Promote Employee')
        print('5. Delete Employee')
        print('6. Exit')
        
        choice = input('Enter your choice: ').strip()
        
        actions = {
            '1': register,
            '2': view,
            '3': edit,
            '4': promote,
            '5': delete,
            '6': exit
        }
        
        actions.get(choice, lambda: print("Invalid option!"))()

if __name__ == "__main__":
    main()
