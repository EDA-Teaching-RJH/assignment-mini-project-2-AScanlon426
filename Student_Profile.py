import json
import statistics

class Student:
    def __init__(self, full_name):
       self.full_name = full_name
       self.username = self._generate_username(full_name)
       self.subjects = {}

    def _generate_username(self, name):
        parts = name.lower().split()
        if len(parts) >= 2:
            return f"{parts[0][0]}{parts[-1]}"
        return name.lower() if name else "unknown"


def main():
    name = input("Enter student's full name: ")
    student = Student(name)
    print(f"Generated Username: {student.username}")

if __name__ == "__main__":
    main()