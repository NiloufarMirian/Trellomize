import json



class User:
    def __init__(self, email, username, password, is_active=True):
        self.email = email
        self.username = username
        self.password = password
        self.is_active = is_active
        self.hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.hashed_password)
    
class SystemManager:
    def __init__(self):
        self.users = []

    def register_user(self, email, username, password):
        if not self.is_valid_email(email):
            print("Invalid email format. Please provide a valid email address.")
            return
        if self.is_duplicate_email(email):
            print("Email already exists. Please use a different email address.")
            return
        if self.is_duplicate_username(username):
            print("Username already exists. Please choose a different username.")
            return
        
        user = User(email, username, password)
        self.users.append(user)
        self.save_data()
        print("User registered successfully.")

    def login(self, username, password):
        user = next((user for user in self.users if user.username == username), None)
        if user and user.password == password and user.is_active:
            print("Login successful.")
        else:
            print("Invalid username or password.")

    def is_valid_email(self, email):
        
        return "@" in email and "." in email

    def is_duplicate_email(self, email):
        return any(user.email == email for user in self.users)

    def is_duplicate_username(self, username):
        return any(user.username == username for user in self.users)

    def save_data(self):
        data = [{"email": user.email, "username": user.username, "password": user.password, "is_active": user.is_active} for user in self.users]
        with open("users.json", "w") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                data = json.load(f)
                self.users = [User(user["email"], user["username"], user["password"], user["is_active"]) for user in data]



def main():
    manager = SystemManager()
    manager.load_data()
    console = Console()

    while True:
        console.print(Panel("Welcome to the User Management System", style="bold magenta"))
        action = Prompt.ask("What would you like to do? [register/login/exit]: ", choices=["register", "login", "exit"])

        if action == "register":
            email = Prompt.ask("Enter your email address: ")
            username = Prompt.ask("Enter your desired username: ")
            password = getpass.getpass(prompt="Enter your password: ")
            manager.register_user(email, username, password)
        elif action == "login":
            username = Prompt.ask("Enter your username: ")
            password = getpass.getpass(prompt="Enter your password: ")
            manager.login(username, password)
        else:
            print("Exiting program.")
            break
