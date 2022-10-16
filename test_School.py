import unittest
import json
from School_methods import School



class TestSchool(unittest.TestCase):

    def test_set_student(self):
        s1 = School()

        student_json = s1.set_student('UnittestStudent', 999)
        
        student = json.loads(student_json)
        
        self.assertNotEqual(student['id'], None)

    def test_set_student_grade(self):
        s2 = School()

        grade_json = s2.set_student_grade(3, 9, 'music')

        grade = json.loads(grade_json) 

        self.assertNotEqual(grade['id'], None)


    def test_set_grade(self):
        s3 = School()

        grade_json = s3.set_grade(3, 6)

        grade = json.loads(grade_json) 

        self.assertNotEqual(grade['id'], None)      


    def test_get_student_by_name(self):
        s4 = School()

        students_json = s4.get_student_by_name('jaime')

        students = json.loads(students_json)

        self.assertNotEqual(students['students'], None)


    def test_get_student_by_id(self):
        s5 = School()

        student_json = s5.get_student_by_id(2)

        student = json.loads(student_json)

        self.assertEqual(student['name'], 'jaime')


    def test_get_student_grades(self):
    
        s6 = School()

        grades_json = s6.get_student_grades(3)

        grades = json.loads(grades_json)

        self.assertEqual(grades['grades'][0]['grade'], 9)


    def test_get_grade(self):
        s7 = School()

        grade_json = s7.get_grade(3)

        grade = json.loads(grade_json)

        self.assertEqual(grade['grade'], 6)


if __name__ == '__main__':
    unittest.main()