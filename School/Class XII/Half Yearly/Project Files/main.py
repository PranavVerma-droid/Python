# Digital Donation Tracker
# A system to track donations, manage donors and NGOs, and match needs with available donations
# By: Pranav Verma (MIT License)

import mysql.connector #type: ignore
from tabulate import tabulate #type: ignore

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789',
    'database': 'donation_tracker'
}

def clear_data():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(f"DROP DATABASE IF EXISTS {config['database']}")
        connection.commit()
        print(f"Database '{config['database']}' has been deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def setup_database():
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password']
        )
        cursor = connection.cursor()
        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
        cursor.execute(f"USE {config['database']}")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors (
            donor_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            phone VARCHAR(20),
            password VARCHAR(100) NOT NULL,
            address TEXT,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # temp
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ngos (
            ngo_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            phone VARCHAR(20),
            password VARCHAR(100) NOT NULL,
            address TEXT,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS donations (
            donation_id INT AUTO_INCREMENT PRIMARY KEY,
            donor_id INT,
            donation_type ENUM('food', 'clothes', 'money') NOT NULL,
            description TEXT,
            quantity INT,
            amount DECIMAL(10,2),
            status ENUM('available', 'matched', 'delivered') DEFAULT 'available',
            donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            request_id INT AUTO_INCREMENT PRIMARY KEY,
            ngo_id INT,
            request_type ENUM('food', 'clothes', 'money') NOT NULL,
            description TEXT,
            quantity INT,
            amount DECIMAL(10,2),
            status ENUM('pending', 'matched', 'fulfilled') DEFAULT 'pending',
            request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (ngo_id) REFERENCES ngos(ngo_id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            match_id INT AUTO_INCREMENT PRIMARY KEY,
            donation_id INT,
            request_id INT,
            match_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (donation_id) REFERENCES donations(donation_id),
            FOREIGN KEY (request_id) REFERENCES requests(request_id)
        )
        """)
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Database setup completed successfully.")
        
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        exit(1)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Failed to connect to database: {err}")
        exit(1)

# WNHY DOES THIS NOT WORK THIS IS STUPUD
def register_donor():
    print("===== DONOR REGISTRATION =====")
    
    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    password = input("Create a password: ")
    confirm_password = input("Confirm password: ")
    
    if password != confirm_password:
        print("Passwords do not match!")
        return
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT email FROM donors WHERE email = %s", (email,))
        if cursor.fetchone():
            print("Email already registered!")
            return
        
        # Insert new donor
        cursor.execute("""
        INSERT INTO donors (name, email, phone, password, address)
        VALUES (%s, %s, %s, %s, %s)
        """, (name, email, phone, password, address))
        
        connection.commit()
        print("Registration successful! You can now log in as a donor.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def register_ngo():
    print("===== NGO REGISTRATION =====")
    
    name = input("Enter NGO name: ")
    email = input("Enter NGO email: ")
    phone = input("Enter NGO phone number: ")
    address = input("Enter NGO address: ")
    password = input("Create a password: ")
    confirm_password = input("Confirm password: ")
    
    if password != confirm_password:
        print("Passwords do not match!")
        return
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT email FROM ngos WHERE email = %s", (email,))
        if cursor.fetchone():
            print("Email already registered!")
            return

        cursor.execute("""
        INSERT INTO ngos (name, email, phone, password, address)
        VALUES (%s, %s, %s, %s, %s)
        """, (name, email, phone, password, address))
        
        connection.commit()
        print("NGO registration successful! You can now log in.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def donor_login():
    print("===== DONOR LOGIN =====")
    
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT donor_id, name FROM donors WHERE email = %s AND password = %s", 
                      (email, password))
        result = cursor.fetchone()
        
        if result:
            return result[0], result[1]
        else:
            print("Invalid email or password!")
            return None, None
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None
    finally:
        cursor.close()
        connection.close()

def ngo_login():
    print("===== NGO LOGIN =====")
    
    email = input("Enter NGO email: ")
    password = input("Enter password: ")
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT ngo_id, name FROM ngos WHERE email = %s AND password = %s", 
                      (email, password))
        result = cursor.fetchone()
        
        if result:
            return result[0], result[1]
        else:
            print("Invalid email or password!")
            return None, None
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None
    finally:
        cursor.close()
        connection.close()

def make_donation(donor_id):
    print("===== MAKE A DONATION =====")
    
    print("Donation Type:")
    print("1. Food")
    print("2. Clothes")
    print("3. Money")
    
    choice = input("Select donation type (1-3): ")
    
    if choice == '1':
        donation_type = "food"
        description = input("Describe the food items (e.g., rice, canned goods): ")
        quantity = int(input("Enter quantity (number of items/packages): "))
        amount = 0
    elif choice == '2':
        donation_type = "clothes"
        description = input("Describe the clothes (e.g., winter jackets, shirts): ")
        quantity = int(input("Enter quantity (number of items): "))
        amount = 0
    elif choice == '3':
        donation_type = "money"
        description = "Monetary donation"
        quantity = 1
        amount = float(input("Enter amount ($): "))
    else:
        print("Invalid choice!")
        return
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO donations (donor_id, donation_type, description, quantity, amount)
        VALUES (%s, %s, %s, %s, %s)
        """, (donor_id, donation_type, description, quantity, amount))
        
        connection.commit()
        print("Donation recorded successfully!")
        
        match_donations_with_requests()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def view_my_donations(donor_id):
    print("===== MY DONATIONS =====")
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        SELECT donation_id, donation_type, description, quantity, amount, status, donation_date
        FROM donations
        WHERE donor_id = %s
        ORDER BY donation_date DESC
        """, (donor_id,))
        
        donations = cursor.fetchall()
        
        if not donations:
            print("You haven't made any donations yet.")
            return
        
        headers = ["ID", "Type", "Description", "Quantity", "Amount ($)", "Status", "Date"]
        table_data = []
        
        for donation in donations:
            date_str = donation[6]
            amount = f"${donation[4]}" if donation[4] else "N/A"
            
            row = [donation[0], donation[1], donation[2], donation[3], 
                  amount, donation[5], date_str]
            table_data.append(row)
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        
    input("\nPress Enter to continue...")

def make_request(ngo_id):
    print("===== MAKE A REQUEST =====")
    
    print("Request Type:")
    print("1. Food")
    print("2. Clothes")
    print("3. Money")
    
    choice = input("Select request type (1-3): ")
    
    if choice == '1':
        request_type = "food"
        description = input("Describe the food items needed: ")
        quantity = int(input("Enter quantity needed: "))
        amount = 0
    elif choice == '2':
        request_type = "clothes"
        description = input("Describe the clothes needed: ")
        quantity = int(input("Enter quantity needed: "))
        amount = 0
    elif choice == '3':
        request_type = "money"
        description = "Money Assist."
        quantity = 1
        amount = float(input("Enter amount needed ($): "))
    else:
        print("Invalid choice!")
        return
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO requests (ngo_id, request_type, description, quantity, amount)
        VALUES (%s, %s, %s, %s, %s)
        """, (ngo_id, request_type, description, quantity, amount))
        
        connection.commit()
        print("Request recorded successfully!")

        match_donations_with_requests()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def view_my_requests(ngo_id):
    print("===== MY REQUESTS =====")
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        SELECT request_id, request_type, description, quantity, amount, status, request_date
        FROM requests
        WHERE ngo_id = %s
        ORDER BY request_date DESC
        """, (ngo_id,))
        
        requests = cursor.fetchall()
        
        if not requests:
            print("You haven't made any requests yet.")
            return
        
        headers = ["ID", "Type", "Description", "Quantity", "Amount ($)", "Status", "Date"]
        table_data = []
        
        for i in requests:
            date_str = i[6]
            amount = f"${i[4]}" if i[4] else "N/A"
            
            row = [i[0], i[1], i[2], i[3], amount, i[5], date_str]
            table_data.append(row)
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        
    input("\nPress Enter to continue...")

def match_donations_with_requests():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        SELECT donation_id, donation_type, quantity, amount
        FROM donations
        WHERE status = 'available'
        """)
        available_donations = cursor.fetchall()
        
        cursor.execute("""
        SELECT request_id, request_type, quantity, amount
        FROM requests
        WHERE status = 'pending'
        """)
        pending_requests = cursor.fetchall()
        
        for i in available_donations:
            donation_id = i
            donation_type = i
            donation_qty = i
            donation_amount = i
            
            matching_requests = [i for i in pending_requests if i[1] == donation_type and i[2] <= donation_qty]
            
            if matching_requests:
                request = matching_requests[0]  # FIRST MATCH REQ.
                request_id = request[0]
                
                # CREATE IT
                cursor.execute("""
                INSERT INTO matches (donation_id, request_id)
                VALUES (%s, %s)
                """, (donation_id, request_id))
                
                # UPDATE THE THING
                cursor.execute("""
                UPDATE donations
                SET status = 'matched'
                WHERE donation_id = %s
                """, (donation_id,))
                
                # UPDATE REQ. THNKS.
                cursor.execute("""
                UPDATE requests
                SET status = 'matched'
                WHERE request_id = %s
                """, (request_id,))
                
                connection.commit()
        
    except mysql.connector.Error as err:
        print(f"Error during matching: {err}")
    finally:
        cursor.close()
        connection.close()

def view_matched_donations(ngo_id):
    print("===== MATCHED DONATIONS =====")
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        SELECT d.donation_id, d.donation_type, d.description, d.quantity, d.amount,
               m.match_date, r.request_id, don.name as donor_name
        FROM matches m
        JOIN donations d ON m.donation_id = d.donation_id
        JOIN requests r ON m.request_id = r.request_id
        JOIN donors don ON d.donor_id = don.donor_id
        WHERE r.ngo_id = %s
        ORDER BY m.match_date DESC
        """, (ngo_id,))
        
        matches = cursor.fetchall()
        
        if not matches:
            print("No matched donations found.")
            return
        
        headers = ["Donation ID", "Type", "Description", "Quantity", "Amount ($)", 
                  "Match Date", "Request ID", "Donor"]
        table_data = []
        
        for i in matches:
            date_str = i[5]
            amount = f"${i[4]}" if i[4] else "N/A"
            
            row = [i[0], i[1], i[2], i[3], amount, date_str, i[6], i[7]]
            table_data.append(row)
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        
    input("\nPress Enter to continue...")

def view_matched_requests(donor_id):
    print("===== MATCHED REQUESTS =====")
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        # TODO: FIX THE FORMATTING: DONE
        cursor.execute("""
        SELECT r.request_id, r.request_type, r.description, r.quantity, r.amount,
               m.match_date, d.donation_id, n.name as ngo_name
        FROM matches m
        JOIN requests r ON m.request_id = r.request_id
        JOIN donations d ON m.donation_id = d.donation_id
        JOIN ngos n ON r.ngo_id = n.ngo_id
        WHERE d.donor_id = %s
        ORDER BY m.match_date DESC
        """, (donor_id,))
        
        matches = cursor.fetchall()
        
        if not matches:
            print("No matched requests found.")
            return
        
        headers = ["Request ID", "Type", "Description", "Quantity", "Amount ($)", 
                  "Match Date", "Donation ID", "NGO"]
        table_data = []
        
        for match in matches:
            date_str = match[5]
            amount = f"${match[4]}" if match[4] else "N/A"
            
            row = [match[0], match[1], match[2], match[3], amount, date_str, match[6], match[7]]
            table_data.append(row)
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        
    input("\nPress Enter to continue...")

def donor_menu(donor_id, donor_name):
    while True:
        print(f"===== DONOR MENU =====")
        print("1. Make a Donation")
        print("2. View My Donations")
        print("3. View Matched Requests")
        print("4. Logout")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            make_donation(donor_id)
        elif choice == '2':
            view_my_donations(donor_id)
        elif choice == '3':
            view_matched_requests(donor_id)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")
        
        if choice != '4':
            input("\nPress Enter to continue...")

def ngo_menu(ngo_id):
    while True:
        print(f"===== NGO MENU =====")
        print("1. Make a Request")
        print("2. View My Requests")
        print("3. View Matched Donations")
        print("4. Logout")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            make_request(ngo_id)
        elif choice == '2':
            view_my_requests(ngo_id)
        elif choice == '3':
            view_matched_donations(ngo_id)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")
        
        if choice != '4':
            input("\nPress Enter to continue...")


setup_database()

while True:
    print("============================")
    print("  DIGITAL DONATION TRACKER  ")
    print("============================")
    print("1. Register as Donor")
    print("2. Register as NGO")
    print("3. Login as Donor")
    print("4. Login as NGO")
    print("5. Clear all Data (Reset)")
    print("6. Exit")
        
    choice = input("Enter your choice (1-5): ")
        
    if choice == '1':
        register_donor()
    elif choice == '2':
        register_ngo()
    elif choice == '3':
        donor_id, donor_name = donor_login()
        if donor_id:
            donor_menu(donor_id, donor_name)
    elif choice == '4':
        ngo_id, ngo_name = ngo_login()
        if ngo_id:
            ngo_menu(ngo_id, ngo_name)
    elif choice == '5':
        clear_data()
        exit(0)
    elif choice == '6':
        exit(0)
    else:
        print("Invalid choice! Please try again")