
from EasyToTravel.config import db
from EasyToTravel.easy_travel.Owner.models import *
from EasyToTravel.easy_travel.Vehicle.models import *

class Driver(db.Model):
    driId = db.Column('driver_id',db.Integer(),primary_key=True)
    driName = db.Column('driver_name',db.String(100))
    driDOB = db.Column('driver_dob',db.String(100))
    driEmail = db.Column('driver_email', db.String(100))
    driMobile = db.Column('driver_cno',db.BIGINT())
    driLiscence = db.Column('driver_liscence',db.Integer())
    driAadhar = db.Column('driver_aadhar',db.BIGINT())
    driRating = db.Column('driver_rating',db.Integer())
    driverOwner = db.relationship('Owner',uselist=False,lazy=True,backref='own_driver')
    driverVehicle = db.Column('driv_veh',db.ForeignKey('vehicle.veh_id'),unique=True)