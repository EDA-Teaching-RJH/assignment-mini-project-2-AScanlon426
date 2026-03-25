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

    def test_calculate_mean(self):
        self.student.add_subject("Maths", 90)
        self.student.add_subject("English", 80)
        self.assertEqual(self.student.calculate_mean(), 85.0)

    def test_calculate_mean_empty(self):
        self.assertEqual(self.student.calculate_mean(), 0.0)

    def test_standard_div(self):
        self.student.add_subject("A", 100)
        self.student.add_subject("B", 0)
        self.assertAlmostEqual(self.student.standard_deviation(), 70.71, places=2)

    def test_standard_deviation_single_subject(self):
        self.student.add_subject("A", 100)
        self.assertEqual(self.student.standard_deviation(), 0.0)
    
    def test_scholarship_eligibility(self):
        sch = Scholarship("Bob Smith")
        sch.add_subject("Math", 84)
        self.assertFalse(sch.is_eligible())
        sch.add_subject("Math", 90) 
        self.assertTrue(sch.is_eligible())