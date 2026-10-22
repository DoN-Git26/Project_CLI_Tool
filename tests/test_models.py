import unittest
from models.user import User
from models.project import Project
from models.task import Task

class TestModels(unittest.TestCase):
    def test_user_project_task(self):
        user = User("Donex Oloo", "donex@example.com")
        project = Project("CLI Tool", "Build CLI", "2026-12-01")
        task = Task("Implement add-task")

        user.add_project(project)
        project.add_task(task)
        task.mark_complete()

        self.assertEqual(task.status, "Complete")
        self.assertEqual(user.projects[0].title, "CLI Tool")

if __name__ == "__main__":
    unittest.main()
