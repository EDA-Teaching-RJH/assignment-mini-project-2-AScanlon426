import json
import statistics
import os

class Student:
    def __init__(self, full_name):
       #initializer method used to set attributes within the Student class
       self.full_name = full_name
       self.username = self._generate_username(full_name)
       self.subjects = {}

    def _generate_username(self, name):
        #function to generate a username given a student's first and last name
        parts = name.lower().split()
        if len(parts) >= 2:
            return f"{parts[0][0]}{parts[-1]}"
        return name.lower() if name else "unknown"

    def add_subject(self, subject, mark):
        #function to add a subject to a student's profile
        self.subjects[subject] = float(mark)

    def calculate_mean(self):
        #function to get a mean from the scores given for each subject
        if not self.subjects:
            return 0.0
        return statistics.mean(self.subjects.values())
    
    def standard_deviation(self):
        #function to get a standard deviation from the scores given for each subject
        if len(self.subjects) < 2:
            return 0.0
        return statistics.stdev(self.subjects.values())

class Scholarship(Student):
    def is_eligible(self):
        #function to determine whether a student is scholarship eligible
        return self.calculate_mean() >= 85.0
    
class Classroom:
    def __init__(self,storage_file="classroom.json"):
        #function to create a file for the data to be saved to
        self.storage_file = storage_file
        self.students = {}

    def add_student(self, student_obj):
        self.students[student_obj.username] = student_obj

    def save_database(self):
        #function to save data to the JSON file
        data = {}
        for uname, s in self.students.items():
         data[uname] = {
             "full_name": s.full_name,
             "username": s.username,
             "subjects": s.subjects,
             "mean_score": s.calculate_mean()
         }
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_database(self):
        #function to turn the saved data into usable pieces of code
        if not os.path.exists(self.storage_file):
            return
        with open(self.storage_file, "r") as f:
            data = json.load(f)
            for uname, info in data.items():
                s = Student(info["full_name"])
                s.subjects = info["subjects"]
                self.students[uname] = s
    
def main():
    #main function to obtain inputs for name, subjects, scores and if the student is applying for a scholarship
    db = Classroom()
    db.load_database()

    name = input("Enter student's full name: ")
    student = Student(name)
    print(f"Generated Username: {student.username}")

    is_sch = input("Has this student applied for a scholarship?").lower() == 'yes'
    student = Scholarship(name) if is_sch else Student(name)

    while True:
        sub = input("Enter subject (or 'done' to exit): ")
        if sub.lower() == 'done': break
        try:
            val = int(input(f"Enter mark for {sub}: "))
            student.add_subject(sub, val)
        except ValueError:
            print("Please enter a valid numeric mark.")

    #prints the final results from the datda collected
    print(f"\nResults for {student.full_name} ({student.username}):")
    print(f"- Average: {student.calculate_mean():.2f}")
    print(f"- Standard Deviation: {student.standard_deviation():.2f}")
    
    if isinstance(student, Scholarship):
        status = "Eligible" if student.is_eligible() else "Ineligible"
        print(f"- Scholarship Status: {status}")

    db.students[student.username] = student
    db.save_database()
    print("\nDatabase updated successfully.")

if __name__ == "__main__":
    main()