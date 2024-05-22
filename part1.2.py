import re
from rich import print as rprint
from datetime import datetime, timedelta
import uuid
import json
import logging
from cryptography.fernet import Fernet

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