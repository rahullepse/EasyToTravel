from EasyToTravel.config import db
from EasyToTravel.easy_travel.Customer.models import *
from EasyToTravel.easy_travel.Vehicle.models import *


class Payment(db.Model):
    payId = db.Column('pay_id',db.Integer(),primary_key=True)
    payMode = db.Column('pay_mode',db.String(50))
    payAmt = db.Column('pay_amt',db.BIGINT())
    payhist = db.relationship('History', uselist=False, lazy=True, backref='pay_hist')
    payCust = db.Column('pay_cust', db.ForeignKey('customer.cust_id'), unique=False)
    payVehicle = db.relationship('Vehicle', uselist=False, lazy=True, backref='pay_veh')
