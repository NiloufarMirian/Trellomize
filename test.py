import unittest
import uuid
from main import Project


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
        # Test removing a user
        user = "test_user"
        self.project.add_user(user)
        self.project.remove_user(user)
        self.assertNotIn(user, self.project.users)

    def test_add_task(self):
        # Test adding a task
        task = "test_task"
        self.project.add_task(task)
        self.assertIn(task, self.project.tasks)


if __name__ == '__main__':
    unittest.main()
