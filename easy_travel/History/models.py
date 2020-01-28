from EasyToTravel.config import db
from EasyToTravel.easy_travel.Customer.models import *
from EasyToTravel.easy_travel.Payment.models import *
from EasyToTravel.easy_travel.Vehicle.models import *
from EasyToTravel.easy_travel.Driver.models import *



class History(db.Column):
    hisId = db.Column('his_id',db.Integer(),primary_key=True)
    histDate = db.Column('hist_date', db.String(100))
    custHist = db.Column('cust_hist', db.ForeignKey('customer.cust_id'), unique=False)
    hisPayment = db.Column('his_payment',db.ForeignKey('payment.pay_id'), unique=True)
    hisVehicle = db.Column('his_vehicle', db.ForeignKey('vehicle.veh_id'), unique=True)
    hisDriver = db.Column('his_driver', db.ForeignKey('driver.driver_id'), unique=True)
