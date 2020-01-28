
from EasyToTravel.config import db
from EasyToTravel.easy_travel.Owner.models import *
from EasyToTravel.easy_travel.Driver.models import *
from EasyToTravel.easy_travel.Trips.models import *
from EasyToTravel.easy_travel.Payment.models import *
from EasyToTravel.easy_travel.History.models import *
from EasyToTravel.easy_travel.Customer.models import *


class Vehicle(db.Model):
    vehId = db.Column('veh_id',db.Integer(),primary_key=True)
    vehName = db.Column('veh_name',db.String(100))
    vehNo = db.Column('veh_no',db.Integer())
    vehSeater = db.Column('veh_seater',db.Integer())
    vehType = db.Column('veh_type',db.String(100))
    vehFueltype = db.Column('veh_fueltype',db.String(100))
    vehRc = db.Column('veh_rc',db.String(100))
    vehPermit = db.Column('veh_permit',db.String(100))
    vehInsurance = db.Column('veh_insurance',db.String(100))
    vehOwner = db.Column('veh_owner', db.ForeignKey('owner.owner_id'), unique=False)
    vehDriver = db.Column('veh_driv', db.ForeignKey('driver.driver_id'), unique=True)
    vehicleCust = db.relationship('Customer',uselist=False,lazy=True,backref='cust_veh')
    vehicleHistory = db.relationship('History', uselist=False, lazy=True, backref='veh_hist')
    vehiclePay = db.Column('vehicle_pay', db.ForeignKey('payment.pay_id'), unique=True)
    vehicleTrip = db.relationship('Trip', uselist=False, lazy=True, backref='veh_trip')