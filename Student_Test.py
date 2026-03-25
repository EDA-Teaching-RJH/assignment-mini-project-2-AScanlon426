import unittest
import json
import os
from unittest.mock import patch, mock_open
from Student_Profile import Student, Scholarship, Classroom

class TestStudentSystem(unittest.TestCase):

    def setup(self):
        self.student = Student("Aaron Scanlon")
        self.classroom = Classroom("classroom_test.json")

    def test_username_format(self):
        self.assertEqual(self.student.username, "ascanlon")

    def test_username_single(self):
        s = Student("John")
        self.asserEqual(s.username, "john")

    def test_username_empty(self):
        s = Student("")
        self.assertEqual(s.username, "unkown")