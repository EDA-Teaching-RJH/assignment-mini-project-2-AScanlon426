import unittest
import json
import os
from unittest.mock import patch, mock_open
from Student_Profile import Student, Scholarship, Classroom

class TestStudentSystem(unittest.TestCase):

    def setup(self):
        self.student = Student("Aaron Scanlon")
        self.classroom = Classroom("classroom_test.json")