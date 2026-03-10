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

    def add_subject(self, subject, mark):
        self.subjects[subject] = float(mark)

    def calculate_mean(self):
        if not self.subjects:
            return 0.0
        return statistics.mean(self.subjects.values())
    
    
def main():
    name = input("Enter student's full name: ")
    student = Student(name)
    print(f"Generated Username: {student.username}")

    while True:
        sub = input("Enter subject (or 'done' to exit): ")
        if sub.lower() == 'done': break
        try:
            val = float(input(f"Enter mark for {sub}: "))
            student.add_subject(sub, val)
        except ValueError:
            print("Please enter a valid numeric mark.")

if __name__ == "__main__":
    main()