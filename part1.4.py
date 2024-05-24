def manage_project(username):
    
    i = 1
    ids = []
    for x in range(len(projects)):
        if projects[x].admin == username:
            projects[x].display(i)
            i = i+1
            ids.append(x)
    if (i == 1):
        print("there is no projects")
        return False
            
    
    while True:
        choice = input("Select: ")
        choice = int(choice)
        if choice < 1 or choice > len(ids):
            rprint("wrong input")
        else:
            id= ids[choice-1]
            break
    
    while True:
        
        rprint("1.Add user")
        rprint("2.Remove user")
        rprint("3.Manage tasks")
        rprint("4.Exit")
        choice = input("Enter your choice (0-4): ")
        if choice == "1":
            user = input("Enter the username you want to add: ")
            if (user in users):
                projects[id].add_user(user)
                rprint("User added successfully") 
            else:
                rprint(f"User {user} not found.")

        if choice == "2":
            user = input("Enter the username you want to remove: ")
            projects[id].remove_user(user)
        
        if choice == "3":
            manage_task(projects[id])

        if choice == "4":
            break

def joined_project(username):

    i = 1
    ids = []
    for x in range(len(projects)):
        if (username in projects[x].users):
            projects[x].display(i)
            i = i+1
            ids.append(x)
    if (i == 1):
        print("there is no projects")
        return False
    while True:
        choice = input("Select: ")
        choice = int(choice)
        if choice < 1 or choice > len(ids):
            rprint("wrong input")
        else:
            project = projects[ids[choice-1]]
            break

    while True:
        rprint("1.All tasks")
        rprint("2.My tasks")
        rprint("3.Exit")
        choice = input("Select: ")
        if choice == "1":
            j = 1
            for i in range(len(tasks)):
                if (project.id == tasks[i].project ):
                    tasks[i].display(j)
                    j += 1

        if choice == "2":
            taskss = []
            j = 1
            for i in range(len(tasks)):
                rprint(tasks[i].users , "   " , username)
                if (project.id == tasks[i].project and (username in tasks[i].users)):
                    tasks[i].display(j)
                    j += 1
                    taskss.append(i)
            
            choice = input("Select: ")
            choice = int(choice)
            if (choice > 0 and choice < j):

                edit_task(tasks[taskss[choice -1]], project)
            else:
                rprint("wrong input")

        if choice == "3":
            break

def user_panel(username):
    while True:
        rprint("1.Create a new project")
        rprint("2.Manage my projects")
        rprint("3.View joined projects")
        rprint("4.Exit")

        choice = input("Enter your choice (0-4): ")
        if choice == "1":
            project = create_project(username)
            projects.append(project)
        if choice == "2":
            manage_project(username)

        if choice == "3":
            joined_project(username)



        if choice == "4":
            break
    
def save_data(filename='data.json'):
    encrypt_all_passwords(users)
    data = {
        'users': users,
        'projects': [project.to_dict() for project in projects],
        'tasks': [task.to_dict() for task in tasks],
    }
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

logging.basicConfig(level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
    filename='app.log', 
    filemode='a')  

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
