from flask import Flask, request, Response
from School_methods import School

app = Flask(__name__)


@app.route('/get-student-by-id', methods=['GET'])
def get_student_by_id_api():

   id = request.args.get('id')

   s = School()

   student = s.get_student_by_id(int(id))
   
   return student

@app.route('/get-student-by-name', methods=['GET'])
def get_student_by_name_api():

   name = request.args.get('name')

   s = School()

   student = s.get_student_by_name(name)
   
   return student

@app.route('/get-student-grades', methods=['GET'])
def get_student_grades_api():

   id = request.args.get('id')

   s = School()

   grades = s.get_student_grades(int(id))
   
   return grades

@app.route('/get-grade', methods=['GET'])
def get_grade_api():

   id = request.args.get('id')

   s = School()

   grade = s.get_grade(int(id))
   
   return grade

@app.route('/set-student', methods=['POST'])
def set_student_api():
   
   try:
      body = request.get_json()  
      
      if 'age' not in body.keys():
         return Response('{"mensagem":"Parâmetro age não encontrado."}', status=400, mimetype='application/json')

      if 'name' not in body.keys():
         return Response('{"mensagem":"Parâmetro name não encontrado."}', status=400, mimetype='application/json')
      
      school = School()

      student = school.set_student(student_name = body['name'], student_age = body['age'])
      
      return Response(student, status=200, mimetype='application/json')

   except Exception as e:
      mensagem = {"mensagem":str(e)}
      return Response(str(mensagem), status=500, mimetype='application/json')




if __name__ == '__main__':
   app.run(port=5000, debug=True)