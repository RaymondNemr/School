from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import Student_and_Grade
import pg8000
import json

Base = Student_and_Grade.Base

engine = create_engine('postgresql+pg8000://postgres:r4ym0nd@localhost:5432/bdprd')

Base.metadata.create_all(engine)

class School:

    def __init__(self):
        
        Session = sessionmaker(bind = engine)
        self.session = Session()


    def set_student(self, student_name, student_age):
        student = Student_and_Grade.Student(name = student_name, age = student_age)
        
        self.session.add(student)
        self.session.commit()
        
        return json.dumps({'id':student.id})

    
    def set_student_grade(self, student_id, grade, subject):

        grade = Student_and_Grade.Grade(student_id = student_id, grade = grade, subject = subject)      
        self.session.add(grade)
        self.session.commit()

        return json.dumps({'id':grade.id})

    
    def set_grade(self, grade_id, new_grade):
        result = self.session.query(Student_and_Grade.Grade).get(grade_id)

        result.grade = new_grade
        self.session.commit()

        return json.dumps({'id':result.id})


    def get_student_by_name(self, student_name):
        result = self.session.query(Student_and_Grade.Student).filter(Student_and_Grade.Student.name == student_name)        
        students_array = [{'name':s.name, 'age':s.age} for s in result]
        dictionary = {'students':students_array}

        return json.dumps(dictionary)
    
    
    def get_student_by_id(self, student_id):
        result = self.session.query(Student_and_Grade.Student).get(student_id)
        
        return json.dumps({'name':result.name, 'age':result.age})
    
    
    def get_student_grades(self, id):
        result = self.session.query(Student_and_Grade.Grade).filter(Student_and_Grade.Grade.student_id==id)
        grades_array = [{'subject':s.subject, 'grade':s.grade} for s in result]
        dictionary = {'grades':grades_array}

        return json.dumps(dictionary)

    
    def get_grade(self, grade_id):
        result = self.session.query(Student_and_Grade.Grade).get(grade_id)

        return json.dumps({'subject':result.subject, 'grade':result.grade})


