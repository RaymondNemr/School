from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
   __tablename__ = 'Students'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   age = Column(Integer)
   

class Grade(Base):
   __tablename__ = 'Grades'
   
   id = Column(Integer, primary_key=True)
   student_id = Column(Integer, ForeignKey('Students.id'))
   subject = Column(String)
   grade = Column(Float)

   student = relationship("Student", back_populates = "Grades")


Student.Grades = relationship("Grade", order_by = Grade.id, back_populates = "student")


