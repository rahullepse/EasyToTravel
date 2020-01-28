
from EasyToTravel.config import db
from EasyToTravel.easy_travel.History.models import *
from EasyToTravel.easy_travel.Vehicle.models import *
from EasyToTravel.easy_travel.Trips.models import *
from EasyToTravel.easy_travel.Owner.models import *


class Driver(db.Model):
    driId = db.Column('driver_id',db.Integer(),primary_key=True)
    driName = db.Column('driver_name',db.String(100))
    driDOB = db.Column('driver_dob',db.String(100))
    driEmail = db.Column('driver_email', db.String(100))
    driMobile = db.Column('driver_cno',db.BIGINT())
    driLiscence = db.Column('driver_liscence',db.Integer())
    driAadhar = db.Column('driver_aadhar',db.BIGINT())
    driRating = db.Column('driver_rating',db.Integer())
    driOwner = db.Column('owner_driv', db.ForeignKey('owner.owner_id'), unique=False)
    driVehic = db.relationship('Vehicle', uselist=False, lazy=True, backref='driv_vehicle')
    driverHistory = db.relationship('History', uselist=False, lazy=True, backref='driv_hist')
    driverTrip = db.relationship('Trip', uselist=True, lazy=True, backref='driv_trip')
