from EasyToTravel.config import db
from EasyToTravel.easy_travel.Driver.models import *
from EasyToTravel.easy_travel.Vehicle.models import *


class Trip(db.Model):
    trId = db.Column('tr_id',db.Integer(),primary_key=True)
    trScr = db.Column('tr_scr',db.String(100))
    trDes = db.Column('tr_des',db.String(100))
    trDate = db.Column('tr_date',db.Integer())
    trDriver = db.Column('tr_driver',db.ForeignKey('driver.driver_id'),unique=False)
    trvehicle = db.Column('tr_vehicle',db.ForeignKey('vehicle.veh_id'),unique=True)
