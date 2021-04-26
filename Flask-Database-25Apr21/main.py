import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> main.py, grab dirctory of file, absolute path of the directory name

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class PatientLog(db.Model):
    patient_id = db.Column(db.Text(9),primary_key = True)
    doctor_in_charge = db.Column(db.Text(25),nullable=False, default='')
    nurse_in_charge = db.Column(db.Text(25),nullable=False, default='')
    diet = db.Column(db.Text(5),nullable=False, default='')
    ambulant = db.Column(db.Text(5),nullable=False, default='')
    code = db.Column(db.Text(10),nullable=False, default='')
    updated_by = db.Column(db.Text(25))
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow(), primary_key = True)

    def __init__(self, patient_id, doctor_in_charge, nurse_in_charge, diet, ambulant, code, updated_by, timestamp):
        self.patient_id = patient_id
        self.doctor_in_charge = doctor_in_charge
        self.nurse_in_charge = nurse_in_charge
        self.diet = diet
        self.ambulant = ambulant
        self.code = code
        self.updated_by = updated_by
        self.timestamp = timestamp

    def __repr__(self):
        return f"{self.patient_id} {self.doctor_in_charge} {self.nurse_in_charge} {self.diet} {self.ambulant} {self.code} {self.updated_by} {self.timestamp}"
