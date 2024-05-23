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

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            rprint(f"User {user} is already in the project.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            rprint(f"User {user} removed.")
        else:
            rprint(f"User {user} is not in the project.")

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            'id': str(self.id),  # Convert UUID to string
            'title': self.title,
            'admin': self.admin,
            'users': self.users,
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(uuid.UUID(data['id']), data['title'], data['admin'])
        project.users = data['users']
        return project
    
class Task:
    def __init__(self,id, project, title, desc, start, end):
        self.id = id
        self.project = project
        self.title = title
        self.desc = desc
        self.start = start
        self.end = end
        self.users = []
        self.prio = "Low"
        self.status = "Backlog"
        self.logs = []
        self.comment = ""

    def display(self , i):
        rprint(f"{i}.Title: {self.title} , description: {self.desc} , Start: {self.start} , End: {self.end}")
        rprint(f"Users: {self.users} , Priority: {self.prio} , Status: {self.status}")
        rprint(f"Log: {self.logs} ")
        rprint(f"Comments:: {self.comment}")

    def add_user(self, user , project):
        if (user in project.users):
            if(user in self.users):
                rprint("this user is currently assigned to this task")
            else:
                self.users.append(user)
                rprint(f"User {user} added")

    def remove_user(self, user):
        if (user in self.users):
            if(user in users):
                self.users.remove(user)
                rprint(f"User {user} removed")
            else:
                rprint(f"User {user} is not in the task.")

    def add_comment(self,comment):
        self.comment = comment
    


    def to_dict(self):
        return {
            'id': str(self.id),  # Convert UUID to string
            'project': str(self.project),
            'title': self.title,
            'desc': self.desc,
            'start': self.start.isoformat(),  # Convert datetime to string
            'end': self.end.isoformat(),
            'users': self.users,
            'prio': self.prio,
            'status': self.status,
            'logs': self.logs,
            'comment': self.comment,

        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(
        id = uuid.UUID(data['id']),
        project=data['project'],
        title=data['title'],
        desc=data['desc'],
        start=datetime.fromisoformat(data['start']),
        end=datetime.fromisoformat(data['end']))

        task.users=data['users'],
        task.prio=data['prio'],
        task.status=data['status'],
        task.logs=data['logs'],
        task.comment=data['comment']
    
        return task
    

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
    

def create_project(username):
    title = input("Enter your project's title: ")
    id = uuid.uuid4()
    rprint("Project created")
    return Project(id,title,username)

def create_task(pid):
    id = uuid.uuid4()
    name = input("Task title: ")
    desc = input("Task description: ")
    start = datetime.now()
    end = start + timedelta(hours=24)
    rprint("Task created")
    return  Task(id, pid, name,desc,start,end)
    
def  edit_task(task , project):

    while True:
        rprint("1.Add user")
        rprint("2.Remove user")
        rprint("3.Change priority")
        rprint("4.Change status")
        rprint("5.Add comment")
        rprint("6.Exit")
        choice = input("Enter your choice (0-6): ")
        

        if choice == "1":
            userr = input("enter username: ")
            task.add_user(userr,project)
            temp = datetime.now()
            temp = temp.isoformat()
            temp = temp + ": user added"
            task.logs.append(temp)
            rprint("user added")

        if choice == "2":
            userr = input("enter username: ")
            task.remove_user(userr)
            temp = datetime.now()
            temp = temp.isoformat()
            temp = temp + ": user removed"
            task.logs.append(temp)
            rprint("user removed")

        if choice == "3":
            while True:
                rprint("1.Critical")
                rprint("2.High")
                rprint("3.Medium")
                rprint("4.Low")
                prio = input("Enter priority: ")
                prio = int(prio)
                if(prio> 0 and prio < 5):
                    if prio == 1:
                        task.prio="Critical"
                    if prio == 2:
                        task.prio="High"
                    if prio == 3:
                        task.prio="Medium"
                    if prio == 4:
                        task.prio="Low"
                
                    temp = datetime.now()
                    temp = temp.isoformat()
                    temp = temp + ": priority changed"
                    task.logs.append(temp)
                    rprint("priority changed")
                    break
                else:
                    rprint("wrong input")

        
        if choice == "4":
            while True:
                rprint("1.BACKLOG")
                rprint("2.TODO")
                rprint("3.DOING")
                rprint("4.DONE")
                rprint("5.ARCHIVED")
                status = input("Enter status: ")
                status = int(status)
                if(status> 0 and status < 6):
                    if status == 1:
                        task.status="BACKLOG"
                    if status == 2:
                        task.status="TODO"
                    if status == 3:
                        task.status="DOING"
                    if status == 4:
                        task.status="DONE"
                    if status == 5:
                        task.status="ARCHIVED"

                    temp = datetime.now()
                    temp = temp.isoformat()
                    temp = temp + ": status changed"
                    task.logs.append(temp)
                    rprint("status changed")
                    break
                else:
                    rprint("wrong input")

        if choice == "5":
            comment = input("Enter your comment: ")
            task.comment=comment
            temp = datetime.now()
            temp = temp.isoformat()
            temp = temp + ": comment added"
            task.logs.append(temp)
            rprint("comment added")

        if choice == "6":
            break

def manage_task(project):
    while True:
        rprint("1.Create task")
        rprint("2.Edit task")
        rprint("3.Exit")
        choice = input("Enter your choice (0-3): ")

        if choice == "1":
        
            task = create_task(project.id)
            tasks.append(task)

        if choice == "2":
            taskss = []
            j = 1
            for i in range(len(tasks)):
                if project.id == tasks[i].project:
                    tasks[i].display(j)
                    taskss.append(i)
                    j += 1
            if (j == 1):
                rprint("there is no tasks")
                continue
            
            choice = input("Select task: ")
            choice = int(choice)
            if (choice > 0 and choice < j):
                edit_task(tasks[taskss[choice -1]], project)
            else:
                rprint("wrong input")



        if choice == "3":
            break