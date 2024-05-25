import json

class Project:
    def __init__(self, id, name, title, leader):
        self.id = id
        self.name = name
        self.title = title
        self.leader = leader
        self.users = []
        self.members = []

    def add_user(self, username):
        if username not in self.users:
            self.users.append(username)
            print(f'User {username} added to the project.')
        else:
            print(f'User {username} is already in the project.')

    def remove_user(self, username):
        if username in self.users:
            self.users.remove(username)
            print(f'User {username} removed from the project.')
        else:
            print(f'User {username} is not in the project.')

    def add_member(self, member_id, member_name, member_title):
        member_info = {"id": member_id, "name": member_name, "title": member_title}
        self.members.append(member_info)
        print(f'User with ID {member_id}, name {member_name}, and title {member_title} was added to the project.')

    @staticmethod
    def check_project_id(project_id):
        try:
            with open("projects.json", "r") as file:
                projects = json.load(file)
                return project_id not in projects
        except FileNotFoundError:
            # If the file does not exist, assume the project ID is valid
            return True

    @staticmethod
    def add_project_to_file(project_id, project_name, project_title):
        new_project = {project_id: {"name": project_name, "title": project_title}}
        try:
            with open("projects.json", "r+") as file:
                data = json.load(file)
                data.update(new_project)
                file.seek(0)
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            # If the file does not exist, create a new one with the new project
            with open("projects.json", "w") as file:
                json.dump(new_project, file, indent=4)

if __name__ == "__main__":
    # Collect project details
    Project_Id = input("Enter project ID: ")
    Project_Name = input("Enter project name: ")
    Project_Title = input("Enter project title: ")
    Leader_Name = input("Enter leader name: ")

    # Create a project instance
    project = Project(Project_Id, Project_Name, Project_Title, Leader_Name)

    # Check if project ID is unique and add project to the file if it is
    if Project.check_project_id(project.id):
        print("The project ID is valid. The project is added to the file.")
        Project.add_project_to_file(project.id, project.name, project.title)
    else:
        print("Duplicate project ID. The project already exists in the file.")

    # Loop to add multiple members
    while True:
        add_member = input("Do you want to add a member to the project? (yes/no): ").strip().lower()
        if add_member == 'yes':
            Member_Id = input("Enter member ID: ")
            Member_Name = input("Enter member name: ")
            Member_Title = input("Enter member title: ")
            project.add_member(Member_Id, Member_Name, Member_Title)
        else:
            break

    # Display the members added to the project
    print("Members in the project:")
    for member in project.members:
        print(member)