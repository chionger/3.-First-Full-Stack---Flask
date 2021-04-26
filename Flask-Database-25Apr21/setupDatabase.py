import datetime
from main import db, PatientLog

db.create_all()

# samuel = PatientLog(111,'physician', 'fall risk',datetime.datetime.utcnow())
# john = PatientLog(112,'dietician', 'nil by mouth',datetime.datetime.utcnow())
#
# print(samuel.id)
# print(john.id)
#
# db.session.add_all([samuel, john])

db.session.commit()

# print(samuel.id)
# print(john.id)
