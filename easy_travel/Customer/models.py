from EasyToTravel.config import db

class Customer(db.Model):
    custId = db.Column('cust_id',db.Integer(),primary_key=True)
    custName = db.Column('cust_name',db.String(100))
    custDOB = db.Column('cust_dob',db.Integer())
    custEmail = db.Column('cust_email',db.String(100))
    custContno = db.Column('cust_cno',db.BigInt())
    vehicle = db.relationship('Customer',uselist=True,lazy=True,backref='custveh')
    address = db.relationship('Customer',uselist=True,
                              secondary='cust_adr',lazy='subquery',
                              backerf=db.backref('cust_veh',lazy=True))
