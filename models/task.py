class Task:
    def __init__(self, title, assigned_to=None):
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to

    def mark_complete(self):
        self.status = "Complete"

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status})"
