from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
  {'id': 1, 'name': 'John', 'age': 20},
  {'id': 2, 'name': 'Jane', 'age': 22},
  {'id': 3, 'name': 'Doe', 'age': 21}
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
@app.route('/students/<int:id>', methods=['GET'])
def get_students(id):
    for student in students:
        if student['id'] == id:
            return jsonify(student)
    return jsonify({'error': 'Student not found'})

# Route to add a new student
# This route will accept a JSON request body with the student details
@app.route('/students', methods=['POST'])
def add_students():
    student = request.get_json()
    new_student = {}
    id = len(students) + 1
    new_student['id'] = id
    new_student['name'] = student.get('name')
    if student.get('age'):
        new_student['age'] = student.get('age')
    else:
        new_student['age'] = 18
    students.append(new_student)
    return jsonify(new_student)

# Route to update an existing student
# This route will accept a JSON request body with the updated student details
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    updated_student = request.get_json()
    for student in students:
        if student['id'] == id:
            if updated_student.get('name'):
                student['name'] = updated_student.get('name')
            return jsonify(student)
    return jsonify({'error': 'Student not found'})

# Route to delete a student
# This route will accept a JSON request body with the student details to be deleted
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_students(id):
    for student in students:
        if student['id'] == id:
            students.remove(student)
            return jsonify(student)
    return jsonify({'error': 'Student not found'})

# Route to delete multiple students
# This route will accept a JSON request body with the list of student IDs to be deleted
@app.route('/students', methods=['DELETE'])
def delete_multiple_students():
    ids = request.get_json().get('ids')
    deleted_students = []
    for student in students:
        if student['id'] in ids:
            students.remove(student)
            deleted_students.append(student)
    return jsonify(deleted_students)

if __name__ == '__main__':
  app.run(debug=True)