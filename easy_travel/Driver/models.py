
from EasyToTravel.config import db

class Driver(db.Model):
    driId = db.Column('driver_id',db.Integer(),primary_key=True)
    driName = db.Column('driver_name',db.String(100))
    driDOB = db.Column('driver_dob',db.String(100))
    driEmail = db.Column('driver_email', db.String(100))
    driMobile = db.Column('driver_cno',db.BigInt())
    driLiscence = db.Column('driver_liscence',db.Integer())
    driAadhar = db.Column('driver_aadhar',db.BigInt())
    driRating = db.Column('driver_rating',db.Integer())
    vehicle = db.relationship('Vehicle',uselist=False,lazy=True,backref='driv_vehicle')
    ownerId = db.Column('owner_id',db.ForeignKey('owner.owner_id'),unique=False,nullable=True)