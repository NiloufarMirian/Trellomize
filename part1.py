import re
from rich import print as rprint
from datetime import datetime, timedelta
import uuid
import json
import logging
from cryptography.fernet import Fernet

key = b"5GPIG0S9hs8AZ7ePycgywCN24ZItBTvqBcU3QAzCEqg="
cipher = Fernet(key)

class Project:
    def __init__(self,id, title, admin):
        self.id = id
        self.title = title
        self.admin = admin
        self.users = []

    def display(self , i):
        rprint(f"{i}.Title: {self.title} , Admin: {self.admin} , Users: {self.users} ")

    def encrypt_password(password):
        encrypted_password = cipher.encrypt(password.encode())
        return encrypted_password.decode()

def encrypt_all_passwords(users):
    for username, user_info in users.items():
        password = user_info['password']
        encrypted_password = encrypt_password(password)
        user_info['password'] = encrypted_password

def decrypt_password(password):
    decrypted_password = cipher.decrypt(password.encode())
    return decrypted_password.decode()

def decrypt_all_passwords(users):
    for username, user_info in users.items():
        encrypted_password = user_info['password']
        decrypted_password = decrypt_password(encrypted_password)
        user_info['password'] = decrypted_password

def load_data(filename='data.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            users = data['users']
            decrypt_all_passwords(users)
            projects = [Project.from_dict(project) for project in data['projects']]
            tasks = [Task.from_dict(task) for task in data['tasks']]
            return users, projects, tasks
    except FileNotFoundError:
        # If the file doesn't exist, return empty data structures
        return {}, [], []


users, projects, tasks = load_data()


def show_menu():
    rprint("Welcome to the User Management System.\nMenu:")
    rprint("1.Create an account")
    rprint("2.Login")
    rprint("3.Save and Exit")

def is_valid_email(email):
    # Basic email validation regex
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def is_valid_username(username):
    # Username must be alphanumeric and between 3 and 20 characters
    return username.isalnum() and 3 <= len(username) <= 20

def is_email_used(email):
    return email in [user['email'] for user in users.values()]

def is_username_used(username):
    return username in users

def register_user(username, email, password):
    if not is_valid_email(email):
        rprint("Invalid email format.")
        return False
    if not is_valid_username(username):
        rprint("Invalid username. It must be alphanumeric and between 3 and 20 characters.")
        return False
    if is_email_used(email):
        rprint("Email is already used.")
        return False
    if is_username_used(username):
        rprint("Username is already taken.")
        return False

    # Register the user
    users[username] = {'email': email, 'password': password , "active":True}
    rprint(f"User {username} registered successfully.")
    return True

def reg():
    while True:
        rprint("\nRegister a new user")
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        if register_user(username, email, password):
            rprint("Registration successful.")
        else:
            rprint("Registration failed. Please try again.")

        
        break

def login_user(username, password):
    if not is_username_used(username):
        rprint("Username does not exist.")
        return False

    if users[username]["active"] == False:
        rprint("This account has been deactivated")

    if users[username]['password'] == password:
        rprint(f"User {username} logged in successfully.")
        return True
    else:
        rprint("Incorrect password.")
        return False



def main():
    
    while True:
        show_menu()
        choice = input("Enter your choice (0-3): ")
        if choice == "1":
            reg()
        
        if choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            if login_user(username, password):
                rprint("Login successful.")
                user_panel(username)
            else:
                rprint("Login failed. Please try again.")

        if choice == "3":
            break
            
    save_data()
                    
if __name__ == "__main__":
    main()
