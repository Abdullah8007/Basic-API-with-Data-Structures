from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
  {'name': 'John', 'age': 20},
  {'name': 'Jane', 'age': 22},
  {'name': 'Doe', 'age': 21}
]

@app.route('/')
def index():
  return '<h1>Helllo World!</h1>'

# Route to get a list of students
# This route will return a JSON response with the list of students
@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(students)

# Route to get a specific student by name
# This route will return a JSON response with the student details
@app.route('/students/<int:age>', methods=['GET'])
def get_students(age):
    for student in students:
        if student['age'] == age:
            return jsonify(student)
    return jsonify({'error': 'Student not found'})

# Route to add a new student
# This route will accept a JSON request body with the student details
@app.route('/students', methods=['POST'])
def add_students():
    student = request.get_json()
    new_student = {}
    new_student['name'] = student['name']
    new_student['age'] = student['age']
    students.append(new_student)
    return jsonify(new_student)

# Route to update an existing student
# This route will accept a JSON request body with the updated student details
@app.route('/students/<int:age>', methods=['PUT'])
def update_student(age):
    updated_student = request.get_json()
    for student in students:
        if student['age'] == age:
            if updated_student.get('name'):
                student['name'] = updated_student.get('name')
            return jsonify(student)
    return jsonify({'error': 'Student not found'})

# Route to delete a student
# This route will accept a JSON request body with the student details to be deleted
@app.route('/students/<int:age>', methods=['DELETE'])
def delete_students(age):
    for student in students:
        if student['age'] == age:
            students.remove(student)
            return jsonify(student)
    return jsonify({'error': 'Student not found'})

if __name__ == '__main__':
  app.run(debug=True)