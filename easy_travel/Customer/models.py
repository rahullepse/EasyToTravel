from EasyToTravel.config import db
from EasyToTravel.easy_travel.Payment.models import *
from EasyToTravel.easy_travel.History.models import *
from EasyToTravel.easy_travel.Vehicle.models import *

class Customer(db.Model):
    custId = db.Column('cust_id',db.Integer(),primary_key=True)
    custName = db.Column('cust_name',db.String(100))
    custDOB = db.Column('cust_dob',db.Integer())
    custEmail = db.Column('cust_email',db.String(100))
    custContno = db.Column('cust_cno',db.BIGINT())
    custVehicle = db.Column('cust_veh', db.ForeignKey('vehicle.veh_id'), unique=True)
    histCust = db.relationship('History', uselist=True, lazy=True, backref='hist_cust')
    custPay = db.relationship('Payment', uselist=True, lazy=True, backref='cust_pay')
