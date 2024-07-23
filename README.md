PASSWORD MANAGER

This is a simple password manager application built with Python, Tkinter, MySQL, and cryptography.
It allows users to securely store and manage their passwords encrypted in a MySQL database.

FEATURES
1.Insert Record: Save usernames, passwords (encrypted), and associated domains into the database.
2.Retrieve Password: Decrypt and display passwords for a given username.
3.List Usernames: Display a list of all usernames stored in the database.
4.Delete Record: Remove a record from the database based on the username.

REQUIREMENTS
Python 3.x
tkinter library
mysql-connector-python library
cryptography library
MySQL server

INSTALLATION
1.Clone the repository:
git clone https://github.com/your_username/password-manager.git
cd password-manager

2.Install the required Python libraries:
pip install -r requirements.txt

3.Set up MySQL database:
Create a MySQL database and table for storing passwords. Replace placeholders in the code with your MySQL connection details and table name.

4.Run the application:
python password_manager.py

USAGE
Launch the application (password_manager.py).
Use the interface to insert new records, retrieve passwords, list usernames, and delete records.

SECURITY NOTES
Encryption: Passwords are encrypted using the Fernet symmetric encryption from the cryptography library before storing them in the database.
Database: Ensure your MySQL server is secure and accessible only to authorized users.

LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.

NOTES:
Replace placeholders:
In the password_manager.py file, replace "your_host_here", "your_username_here", "your_password_here", "your_database_name_here", and "your_table_name_here" with your actual MySQL database details and table name.
Dependencies: 
Ensure the requirements.txt file includes all necessary dependencies (tkinter, mysql-connector-python, cryptography). If any additional libraries are used, add them to this file.
License: Adjust the license section (LICENSE file) according to your preferences or project requirements.
