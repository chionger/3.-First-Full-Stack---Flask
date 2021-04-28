import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, SubmitField, SelectField
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy
import datetime

# Create a Flask Instance
app = Flask(__name__)

# Add Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

print(basedir)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///working_data.sqlite'
# Secret Key
app.config['SECRET_KEY'] = 'mykey'

# initialize database
db = SQLAlchemy(app)

# Create Model
class PatientLog(db.Model):

    patient_id = db.Column(db.Text(9),primary_key = True)
    doctor_in_charge = db.Column(db.Text(25),nullable=False, default='')
    nurse_in_charge = db.Column(db.Text(25),nullable=False, default='')
    diet = db.Column(db.Text(5),nullable=False, default='')
    ambulant = db.Column(db.Text(5),nullable=False, default='')
    fallrisk = db.Column(db.Text(5), nullable=False,
    default='')
    code = db.Column(db.Text(10),nullable=False, default='')
    updated_by = db.Column(db.Text(25))
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow(), primary_key = True)

class InputForm(FlaskForm):

    patient_id = SelectField(label = 'Patient ID: ', choices = [('Adam', 'Adam'), ('Eve', 'Eve'), ('Eva', 'Eva'), ('Henry', 'Henry'), ('Mark', 'Mark'), ("", "---")], default = "", validators=[InputRequired('Patient ID is required')])

    doctor_in_charge = SelectField(label = 'Doctor_in_charge : ', choices = [('Dr A', 'Dr A'), ('Dr B', 'Dr B'), ('Dr C', 'Dr C'), ('Dr D', 'Dr D'), ('Dr E', 'Dr E'), ("", "---")], default = "")

    nurse_in_charge = SelectField(label = 'Nurse_in_charge : ', choices = [('Nurse A', 'Nurse A'), ('Nurse B', 'Nurse B'), ('Nurse C', 'Nurse C'), ('Nurse D', 'Nurse D'), ('Nurse E', 'Nurse E'), ("", "---")], default="")

    diet = SelectField(label = 'Diet : ', choices = [('DOC', 'DOC'), ('NBM', 'NBM'), ("", "---")], default="")

    ambulant = SelectField(label = 'Ambulant : ', choices = [('Wheelchair', 'Wheelchair'), ('Not required', 'Not required'), ("", "---")], default="")

    fallrisk = SelectField(label = 'Fall Risk :', choices =[('Yes','Yes'),('No','No'),("", "---")],
    default ="")

    code = SelectField(label = 'Code : ', choices = [('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GREEN', 'GREEN'), ("", "---")], default="")

    updated_by = SelectField(label = 'Updated by : ', choices = [('COW Terminal 1', 'COW Terminal 1'), ('COW Terminal 2', 'COW Terminal 2'), ('COW Terminal 3', 'COW Terminal 3'), ('COW Terminal 4', 'COW Terminal 4'), ('COW Terminal 5', 'COW Terminal 5')])

    # timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow(), primary_key = True)
    submit = SubmitField('Save')

class PatientCentricDisplayForm(FlaskForm):
    patient = SelectField(label = 'Patient : ', choices = [('Adam', 'Adam'), ('Eve', 'Eve'), ('Eva', 'Eva'), ('Henry', 'Henry'), ('Mark', 'Mark'), ("", "---")], default = "",  validators=[InputRequired('Patient ID is required')])
    proceed = SubmitField('Display')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        # no check for duplication as probability of a collision based on the composite primary key of patient_id and timestamp is low and acceptable.
        pre_existing_patient_info = PatientLog.query.filter_by(patient_id = form.patient_id.data).order_by(PatientLog.timestamp.desc()).first()

        # no need to do for patient_id as must be provided.
        # how about in the beginning when there is no patient record ? how to take care of that case ?
        if form.doctor_in_charge.data != '':
            new_doctor_in_charge = form.doctor_in_charge.data
        elif pre_existing_patient_info:
            new_doctor_in_charge = pre_existing_patient_info.doctor_in_charge
        else: # means not in existing record
            new_doctor_in_charge = 'To be updated'

        if form.nurse_in_charge.data != '':
            new_nurse_in_charge = form.nurse_in_charge.data
        elif pre_existing_patient_info:
            new_nurse_in_charge = pre_existing_patient_info.nurse_in_charge
        else:
            new_nurse_in_charge = 'To be updated'

        if form.diet.data != '':
            new_diet = form.diet.data
        elif pre_existing_patient_info:
            new_diet = pre_existing_patient_info.diet
        else:
            new_diet = 'To be updated'

        if form.ambulant.data != '':
            new_ambulant = form.ambulant.data
        elif pre_existing_patient_info:
            new_ambulant = pre_existing_patient_info.ambulant
        else:
            new_ambulant = 'To be updated'

        if form.fallrisk.data != '':
            new_fallrisk = form.fallrisk.data
        elif pre_existing_patient_info:
            new_fallrisk = pre_existing_patient_info.fallrisk
        else:
            new_fallrisk = 'To be updated'

        if form.code.data != '':
            new_code = form.code.data
        elif pre_existing_patient_info:
            new_code = pre_existing_patient_info.code
        else:
            new_code = 'To be updated'

        if form.updated_by.data != '':
            new_updated_by = form.updated_by.data
        elif pre_existing_patient_info:
            new_updated_by = pre_existing_patient_info.updated_by
        else:
            new_updated_by = 'To be updated'

        patient = PatientLog(
        patient_id= form.patient_id.data,
        doctor_in_charge = new_doctor_in_charge,
        nurse_in_charge = new_nurse_in_charge,
        diet = new_diet,
        ambulant = new_ambulant,
        fallrisk = new_fallrisk,
        code = new_code,
        updated_by = new_updated_by,

        timestamp=datetime.datetime.utcnow()
        )
        db.session.add(patient)
        db.session.commit()

        session['patient_id']=form.patient_id.data
        session['doctor_in_charge']=form.doctor_in_charge.data
        session['nurse_in_charge']=form.nurse_in_charge.data
        session['diet']=form.diet.data
        session['ambulant']=form.ambulant.data
        session['fallrisk']=form.fallrisk.data
        session['code']=form.code.data
        session['updated_by']=form.updated_by.data

        return redirect(url_for('update_display'))
    return render_template('canary3-index.html', form = form)

@app.route('/update_display')
def update_display():
    cumulogs = PatientLog.query.order_by(PatientLog.timestamp)
    # cumulogs = PatientLog.query.filter_by(patient_id = form.patient_id.data)
    return render_template('canary3-update_display.html', cumulogs = cumulogs)

@app.route('/individual_screen')
def individual_screen():
    cumulogs = PatientLog.query.filter_by(patient_id = 'Adam').order_by(PatientLog.timestamp)
    return render_template('canary3-update_display.html', cumulogs=cumulogs)

@app.route('/select_patient_centric_display', methods = ['POST', 'GET'])
def select_patient_centric_display():
    form = PatientCentricDisplayForm()
    if form.validate_on_submit():
        cumulogs = PatientLog.query.filter_by(patient_id =form.patient.data).order_by(PatientLog.timestamp.desc())
        if cumulogs.count() == 0:
            return '<h1>There is no record on patient ' + form.patient.data + ' in the database.</h1>'
        else:
            return render_template('patient_dashboard1.html', cumulogs=cumulogs)
    return render_template('select_patient_centric_display.html', form = form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('canary3-404.html')

    # deactivate when not in Pi
if __name__ == '__main__':
    app.run(debug = True)

    # remove remark when in Pi
    # app.run(host='0.0.0.0', port = 8000, debug = True)
