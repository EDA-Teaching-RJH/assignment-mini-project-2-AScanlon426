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

    def test_add_student_to_classroom(self):
        self.classroom.add_student(self.student)
        self.assertIn("jdoe", self.classroom.students)
        self.assertEqual(self.classroom.students["jdoe"].full_name, "Jane Doe")

    def test_save_database_writes_correct_json(self, mocked_file):
        self.student.add_subject("Math", 100)
        self.classroom.add_student(self.student)
        self.classroom.save_database()
        
        mocked_file.assert_called_once_with("test_classroom.json", "w")
        
        written_data = "".join(call.args[0] for call in mocked_file().write.call_args_list)
        data = json.loads(written_data)
        self.assertEqual(data["jdoe"]["full_name"], "Jane Doe")

if __name__ == "__main__":
    unittest.main()