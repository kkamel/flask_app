
import csv
import sqlite3
import time

from datetime import datetime
from dask import dataframe as dd
from markupsafe import escape

from flask import Flask, current_app, g, render_template
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from .models import db, Student


app = Flask(__name__)
api = Api(app)

#DATABASE = '/path/to/database.db'
data_file = "lie_sentiment_review.csv"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
# Intialize DB
#db = SQLAlchemy(app)

# Data files
fields = []
rows = []


@app.before_first_request
def create_tables():
    #read_csv(data_file)
    read_verylarge_csv(data_file)
    db.init_app(app)
    db.create_all()


'''
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
'''
parser = reqparse.RequestParser()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/students', methods=["GET"])
def list_students():
    "in list_students"
    result = Student.query.order_by(Student.name).all()
    students = {}
    for student in result:
        students[student.id] = (student.name, student.age, student.spec)
    
    return str(result), 200
   

@app.route('/students', methods=["POST"])
def add_new_student():
    # Request args need to be parsed
    parser.add_argument("name")
    parser.add_argument("age")
    parser.add_argument("spec")
    args = parser.parse_args()
    #----Parse request args------
    new_name = ""
    new_age = ""
    new_spec = ""
    if "name" in args:
        new_name = args["name"]
    if "age" in args:
        new_age = args["age"]
    if "spec" in args:
        new_spec = args["spec"]
    #-----Create new student object---------
    result = Student.query.filter_by(name=new_name).first()
    # Check is student already exists in table
    if result:
        return "Student already exists!", 200
    # If student does not exist, create a new student object
    new_student = Student(name=new_name, age=new_age, spec=new_spec)
    try:
        #-----Add new student object---------
        db.session.add(new_student)
        #-----Commit new student object---------
        db.session.commit()
        result = Student.query.filter_by(name=new_name).first()
        return str(result), 201
    except:
        return "Could not add new student to DB", 500

@app.route('/students/<student_id>', methods=["GET"])
def retrieve_student(student_id):
    result = Student.query.get(student_id)
    print(result)
    if not result:
        return "Student Not found", 404    
    return str(result), 200


@app.route('/students/<student_id>', methods=["PUT"])
def update_student(student_id):
    # Retrieve student tuple from db
    student = Student.query.get(student_id)
    if not student:
        return "Record not found", 404
    parser.add_argument("name")
    parser.add_argument("age")
    parser.add_argument("spec")
    args = parser.parse_args()  
    # Modify student tuple
    student.name = args["name"] if args["name"] is not None else student["name"]
    student.age = args["age"] if args["age"] is not None else student["age"]
    student.spec = args["spec"] if args["spec"] is not None else student["spec"]
    # Commit modified tuple to db
    db.session.commit()
    return str(student), 200


@app.route('/students/<student_id>', methods=["DELETE"])
def remove_student(student_id):
    # Retrieve student tuple from db
    student = Student.query.get(student_id)
    if not student:
        return "Record not found", 404
    db.session.delete(student)
    db.session.commit()
    return '', 204


def read_csv(filepath):
    print("read csv")
    # reading csv file
    with open(filepath, 'r') as csvfile:
        # create a csv reader object
        csvreader = csv.reader(csvfile)
          
        # extract fields from first line
        fields = next(csvreader)
      
        # extract each line
        for row in csvreader:
            rows.append(row)
      
        # get total number of rows
        print("Total no. of rows: %d"%(csvreader.line_num))
    
    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

''' Dask utilizes multiple CPU cores by internally chunking dataframe and process in parallel.
 It can be parallelized on a single machine or distributed processing system. Dask uses
lazy computation by creating a graph of tasks and then invokes a compute() function when invoked.
'''  
def read_verylarge_csv(filepath):
    start = time.time()
    dask_df = dd.read_csv(filepath)
    end = time.time()
    print("Read csv with dask: ",(end-start),"sec")

'''
api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')
'''
if __name__ == "__main__":
    create_tables()
    app.run(host='localhost', port=5000, debug=True)

