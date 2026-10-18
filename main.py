import argparse
from utils.storage import load_data, save_data
from models.user import User
from models.project import Project
from models.task import Task

def add_user(name, email):
    data = load_data()
    user = {"name": name, "email": email, "projects": []}
    data["users"].append(user)
    save_data(data)
    print(f"✅ User {name} added.")

def list_users():
    data = load_data()
    for user in data["users"]:
        print(f"- {user['name']} ({user['email']})")

def add_project(user_name, title, description, due_date):
    data = load_data()
    for user in data["users"]:
        if user["name"] == user_name:
            project = {"title": title, "description": description, "due_date": due_date, "tasks": []}
            user["projects"].append(project)
            save_data(data)
            print(f"✅ Project {title} added to {user_name}.")
            return
    print("❌ User not found.")

def add_task(project_title, task_title, assigned_to=None):
    data = load_data()
    for user in data["users"]:
        for project in user["projects"]:
            if project["title"] == project_title:
                task = {"title": task_title, "status": "Pending", "assigned_to": assigned_to}
                project["tasks"].append(task)
                save_data(data)
                print(f"✅ Task {task_title} added to {project_title}.")
                return
    print("❌ Project not found.")

def complete_task(project_title, task_title):
    data = load_data()
    for user in data["users"]:
        for project in user["projects"]:
            if project["title"] == project_title:
                for task in project["tasks"]:
                    if task["title"] == task_title:
                        task["status"] = "Complete"
                        save_data(data)
                        print(f"✅ Task {task_title} marked complete.")
                        return
    print("❌ Task not found.")

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # add-user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)
    user_parser.add_argument("--email", required=True)

    # list-users
    subparsers.add_parser("list-users")

    # add-project
    project_parser = subparsers.add_parser("add-project")
    project_parser.add_argument("--user", required=True)
    project_parser.add_argument("--title", required=True)
    project_parser.add_argument("--description", required=True)
    project_parser.add_argument("--due_date", required=True)

    # add-task
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("--project", required=True)
    task_parser.add_argument("--title", required=True)
    task_parser.add_argument("--assigned_to")

    # complete-task
    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("--project", required=True)
    complete_parser.add_argument("--title", required=True)

    args = parser.parse_args()

    if args.command == "add-user":
        add_user(args.name, args.email)
    elif args.command == "list-users":
        list_users()
    elif args.command == "add-project":
        add_project(args.user, args.title, args.description, args.due_date)
    elif args.command == "add-task":
        add_task(args.project, args.title, args.assigned_to)
    elif args.command == "complete-task":
        complete_task(args.project, args.title)

if __name__ == "__main__":
    main()
