import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from cryptography.fernet import Fernet

# Generate a Fernet key
encryption_key = b'hOj1NkmmBjYPqSXBmfPwYe8n7WAsjy1wP8sBpvoPCA4='

# Initialize Fernet with the encryption key
cipher_suite = Fernet(encryption_key)

def encrypt_password(password):
    # Encrypt password
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    # Decrypt password
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

def insert_into_db():
    username = username_entry.get()
    password = password_entry.get()
    domain = domain_entry.get()  # Retrieve domain from entry field

    # Encrypt the password before inserting into the database
    encrypted_password = encrypt_password(password)

    try:
        conn = mysql.connector.connect(
            host="your_host_here",
            user="your_username_here",
            password="your_password_here",
            database="your_database_name_here"
        )

        if conn.is_connected():
            cursor = conn.cursor()
            sql_insert_query = "INSERT INTO your_table_name_here (username, passwords, domain) VALUES (%s, %s, %s)"
            insert_tuple = (username, encrypted_password, domain)  # Include domain in insert tuple
            cursor.execute(sql_insert_query, insert_tuple)
            conn.commit()
            messagebox.showinfo("Success", "Record inserted successfully")
            cursor.close()
            conn.close()

    except Error as e:
        messagebox.showerror("Error", f"Error while connecting to MySQL or executing query: {e}")

def retrieve_from_db():
    username = username_entry.get()

    try:
        conn = mysql.connector.connect(
            host="your_host_here",
            user="your_username_here",
            password="your_password_here",
            database="your_database_name_here"
        )

        if conn.is_connected():
            cursor = conn.cursor()
            sql_retrieve_query = "SELECT passwords FROM your_table_name_here WHERE username = %s"
            cursor.execute(sql_retrieve_query, (username,))
            encrypted_password = cursor.fetchone()

            if encrypted_password:
                encrypted_password = encrypted_password[0]
                # Decrypt the retrieved password
                decrypted_password = decrypt_password(encrypted_password)
                if decrypted_password:
                    messagebox.showinfo("Password", f"Password for {username}: {decrypted_password}")
                else:
                    messagebox.showerror("Error", "Failed to decrypt password")
            else:
                messagebox.showerror("Error", "Username not found")

            cursor.close()
            conn.close()

    except Error as e:
        messagebox.showerror("Error", f"Error while connecting to MySQL or executing query: {e}")

def retrieve_usernames():
    try:
        conn = mysql.connector.connect(
            host="your_host_here",
            user="your_username_here",
            password="your_password_here",
            database="your_database_name_here"
        )

        if conn.is_connected():
            cursor = conn.cursor()
            sql_retrieve_query = "SELECT username FROM your_table_name_here"
            cursor.execute(sql_retrieve_query)
            usernames = cursor.fetchall()

            if usernames:
                username_list = "\n".join([username[0] for username in usernames])
                messagebox.showinfo("Usernames", f"List of usernames:\n{username_list}")
            else:
                messagebox.showinfo("Usernames", "No usernames found in the database")

            cursor.close()
            conn.close()

    except Error as e:
        messagebox.showerror("Error", f"Error while connecting to MySQL or executing query: {e}")

def delete_from_db():
    username_to_delete = delete_entry.get()

    try:
        conn = mysql.connector.connect(
            host="your_host_here",
            user="your_username_here",
            password="your_password_here",
            database="your_database_name_here"
        )

        if conn.is_connected():
            cursor = conn.cursor()
            sql_delete_query = "DELETE FROM your_table_name_here WHERE username = %s"
            cursor.execute(sql_delete_query, (username_to_delete,))
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Record for {username_to_delete} deleted successfully")
            else:
                messagebox.showerror("Error", f"No record found for username {username_to_delete}")

            cursor.close()
            conn.close()

    except Error as e:
        messagebox.showerror("Error", f"Error while connecting to MySQL or executing query: {e}")

# Create the main window
root = tk.Tk()
root.geometry("600x400")
root.title("PASSWORD MANAGER")

# Create labels and entry widgets for username, password, and domain
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

username_entry = tk.Entry(root, width=40)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

password_entry = tk.Entry(root, show="*", width=40)
password_entry.grid(row=1, column=1, padx=10, pady=10)

domain_label = tk.Label(root, text="Domain:")
domain_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

domain_entry = tk.Entry(root, width=40)
domain_entry.grid(row=2, column=1, padx=10, pady=10)

delete_label = tk.Label(root, text="Delete Record:")
delete_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

delete_entry = tk.Entry(root, width=40)
delete_entry.grid(row=5, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Record", command=delete_from_db)
delete_button.grid(row=5, column=2, padx=10, pady=10, sticky="e")

# Create buttons for insert and retrieve operations
insert_button = tk.Button(root, text="Insert Record", command=insert_into_db)
insert_button.grid(row=3, column=1, padx=10, pady=20, sticky="w")

retrieve_button = tk.Button(root, text="Retrieve Password", command=retrieve_from_db)
retrieve_button.grid(row=3, column=1, padx=10, pady=20, sticky="e")

list_button = tk.Button(root, text="List Usernames", command=retrieve_usernames)
list_button.grid(row=4, column=1, padx=10, pady=20, sticky="e")

# Start the Tkinter main loop
root.mainloop()
