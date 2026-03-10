import json
import statistics

class Student:
    def __init__(self, full_name):
       self.full_name = full_name
       self.username = self._generate_username(full_name)
       self.subjects = {}


def main():
    name = input("Enter student's full name: ")

if __name__ == "__main__":
    main()