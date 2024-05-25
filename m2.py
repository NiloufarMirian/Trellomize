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