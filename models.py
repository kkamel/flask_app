from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
# Intialize DB
db = SQLAlchemy()
#db.Model.metadata.reflect(db.engine)

class Student(db.Model):
    __tablename__ = 'Students'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    age = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=False
    )
    spec = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    
    def __repr__(self):
        return f"Student('{self.id}', '{self.name}', '{self.age}', '{self.spec}')"
'''
class School(db.Model):
    __tablename__ = 'schools-geocoded'
    __table_args__ = { 'extend_existing': True }
    LOC_CODE = db.Column(db.Text, primary_key=True)
'''

