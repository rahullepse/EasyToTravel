
from EasyToTravel.config import db
from EasyToTravel.easy_travel.Owner.models import *
from EasyToTravel.easy_travel.Driver.models import *


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
    ownerVehic = db.relationship('Owner',uselist=False,lazy=True,backref='own_vehicle')
    vehDriver = db.relationship('Driver', uselist=False, lazy=True, backref='driv_vehicle')
    vehicleCust = db.relationship('Customer',uselist=False,lazy=True,backref='cust_veh')