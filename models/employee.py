import uuid
from datetime import datetime

class Employee:
    def __init__(self, first_name, last_name, role, branch="Main"):
        self.employee_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.branch = branch
        self.created_at = datetime.now()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role,
            "branch": self.branch,
            "created_at": self.created_at.isoformat()
        }
