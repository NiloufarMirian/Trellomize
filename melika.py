Melika, [May 19, 2024 at 21:00]
import json

class Project:
    def __init__(self, id, name, title):
        self.id = id
        self.name = name
        self.title = title

    def check_project_id(project_id):
        with open("projects.json", "r") as file:
            projects = json.load(file)
            if project_id in projects:
                return False
            else:
                return True

    def add_project_to_file(project_id, project_name, project_title):
        new_project = {project_id: {"name": project_name, "title": project_title}}
        with open("projects.json", "r+") as file:
            data = json.load(file)
            data.update(new_project)
            file.seek(0)
            json.dump(data, file, indent=4)

Project
project = Project(1,”1", “Project 1”, “Project title 1")

if Project.check_project_id(project.id):
    print("The project ID is valid. The project is added to the file.")
    Project.add_project_to_file(project.id, project.name, project.title)
else:
    print("The ID of the duplicate project. The project already exists in the file.")

def add_member(self, member_id, member_name, member_title):
        member_info = {"id": member_id, "name": member_name, "title": member_title}
        self.members.append(member_info)
        print(f”user with id{member_id} and with name{member_name} and with title{member_title} was added to the project”)

project.add_member(1,”member1” , “title1”)
project.add_member(2, "member 2” , “title2”)
project.add_member(3, "member3” , “title3”)
