from enum import Enum
from datetime import datetime
import uuid

class Priority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

class Status(Enum):
    BACKLOG = 1
    TODO = 2
    DOING = 3
    DONE = 4
    ARCHIVED = 5

class Task:
    def __init__(self, name, priority=Priority.LOW, status=Status.BACKLOG):
        self.name = name
        self._priority = priority
        self._status = status
        self.assignee = None
        self.start_date = None
        self.end_date = None
        self.task_id = uuid.uuid4()

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, new_priority):
        if isinstance(new_priority, Priority):
            self._priority = new_priority
        else:
            raise ValueError("Priority must be a Priority enum value.")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if isinstance(new_status, Status):
            self.new_status = new_status
        else:
            raise ValueError("Status must be a Status enum value.")

class Member:
    def __init__(self, name):
        self.name = name

class ProjectManager:
    def __init__(self, members, admin):
        self.members = members
        self.admin = admin
        self.tasks = {}

    def assign_task(self, task, assignee):
        task.assignee = assignee
        task.start_date = datetime.now()
        #self.tasks.append(task)

admin = Member("Admin")
member1 = Member("Alice")
member2 = Member("Bob")

project_manager = ProjectManager([member1, member2], admin)

task1 = Task("Task 1", Priority.HIGH, Status.TODO)
task2 = Task("Task 2", Status.DOING)

project_manager.assign_task(task1, member1)
project_manager.assign_task(task2, member2)

task1.priority = Priority.CRITICAL

#project_manager.tasks()
print(f"Task: {task1.name}")
print(f"Priority: {task1.priority.name}")
print(f"Status: {task1.status.name}")
print(f"Assignee: {task1.assignee.name}")
print(f"Start Date: {task1.start_date}")
print(f"End Date: {task1.end_date}")
print(f"Task ID: {task1.task_id}")
print()
