import unittest
import uuid
from datetime import datetime, timedelta
from main import Project, Task

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project_id = uuid.uuid4()
        self.title = "Test Project"
        self.admin = "admin_user"
        self.project = Project(self.project_id, self.title, self.admin)

    def test_add_user(self):
        # Test adding a user
        user = "test_user"
        self.project.add_user(user)
        self.assertIn(user, self.project.users)

    def test_remove_user(self):
        # test removing a user
        user = "test_user"
        self.project.add_user(user)
        self.project.remove_user(user)
        self.assertNotIn(user, self.project.users)

    def test_add_task(self):
        # test adding a task
        task = "test_task"
        self.project.add_task(task)
        self.assertIn(task, self.project.tasks)

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task_id = uuid.uuid4()
        self.project_id = uuid.uuid4()
        self.title = "Test Task"
        self.desc = "This is a test"
        self.start = datetime.now()
        self.end = self.start + timedelta(days=1)
        self.users = []
        self.prio = 1
        self.status = "important"
        self.logs = []
        self.comment = "comments"
        self.task = Task(self.task_id,self.project_id,self.title,self.desc,self.start,self.end,self.users, self.prio, self.status, self.logs, self.comment)

    def test_add_user(self):
        # Test adding a user
        user = "test_user"
        self.task.add_user(user)
        self.assertIn(user, self.task.users)

    def test_remove_user(self):
        # Test removing a user
        user = "test_user"
        self.task.add_user(user)
        self.task.remove_user(user)
        self.assertNotIn(user, self.task.users)

    def test_update_status(self):
        # Test updating the status
        new_status = "Done"
        self.task.update_status(new_status)
        self.assertEqual(self.task.status, new_status)

    def test_add_log(self):
        # Test adding a log
        log = "This is a test for log."
        self.task.add_log(log)
        self.assertIn(log,self.task.logs)

if __name__ == '__main__':
    unittest.main(exit=False)
