from EasyToTravel.config import db
from EasyToTravel.easy_travel.Vehicle.models import *
from EasyToTravel.easy_travel.Driver.models import *

class Owner(db.Model):
    ownId = db.Column('owner_id',db.Integer(),primary_key=True)
    ownName = db.Column('owner_name',db.String(100))
    ownAge = db.Column('owner_age',db.Integer())
    ownDOB = db.Column('owner_dob',db.String(100))
    ownEmail = db.Column('owner_email', db.String(100))
    ownMobileno = db.Column('owner_cno',db.BIGINT())
    ownPan = db.Column('owner_pan',db.String(100))
    ownAadhar = db.Column('owner_aadhar', db.BIGINT())
    ownerVehic = db.relationship('Vehicle', uselist=True, lazy=True, backref='own_vehicle')
    ownerDriver = db.relationship('Driver', uselist=True, lazy=True, backref='own_driver')

