import json
import statistics

class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.username = self._generate_username(full_name)
        self.subjects = {}

    def _generate_username(self, name):
        """Logic: First initial + last name (e.g., 'John Doe' -> 'jdoe')."""
        parts = name.lower().split()
        if len(parts) >= 2:
            return f"{parts[0][0]}{parts[-1]}"
        return name.lower() if name else "unknown"

    def add_subject(self, subject, mark):
        """Adds a subject and validates that the mark is a number."""
        self.subjects[subject] = float(mark)

    def calculate_mean(self):
        """Calculates mean using the statistics library."""
        if not self.subjects:
            return 0.0
        return statistics.mean(self.subjects.values())

    def save_to_file(self, filename="profile.json"):
        """Saves the profile data to a JSON file (File I/O)."""
        data = {
            "full_name": self.full_name,
            "username": self.username,
            "subjects": self.subjects,
            "mean_score": self.calculate_mean()
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

def main():
    name = input("Enter Student Full Name: ")
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