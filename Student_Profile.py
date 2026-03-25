import json
import statistics
import os

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
    
    def standard_deviation(self):
        if len(self.subjects) < 2:
            return 0.0
        return statistics.stdev(self.subjects.values())

class Scholarship(Student):
    def is_eligible(self):
        return self.mean_score >= 85.0
    
class Classroom:
    def __init__(self,storage_file="classroom.json"):
        self.storage_file = storage_file
        self.students = {}

    def add_student(self, student_obj):
        self.students[student_obj.username] = student_obj

    def save_database(self):
        data = {
            "full_name": self.full_name,
            "username": self.username,
            "subjects": self.subjects,
            "mean_score": self.calculate_mean()
        }
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_database(self):
        if not os.path.exists(self.storage_file):
            return
        with open(self.storage_file, "r") as f:
            data = json.load(f)
            for uname, info in data.items():
                s = Student(info["name"])
                s.subjects = info["marks"]
                self.students[uname] = s
    
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

    student.save_to_file()
    print(f"Profile saved! Average score: {student.calculate_mean():.2f}")

if __name__ == "__main__":
    main()