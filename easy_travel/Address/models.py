from EasyToTravel.config import db
from EasyToTravel.easy_travel.Owner.models import *
from EasyToTravel.easy_travel.Customer.models import *

ownerAdrs = db.Table('OwnerAdrs',
                  db.Column('ownerId',db.Integer(),db.ForeignKey('owner.owner_id'),unique=False,primary_key=True),
                  db.Column('adrsId',db.Integer(),db.ForeignKey('address.adr_id'),unique=False,primary_key=True))

custAdrs = db.Table('CustAdrs',
                  db.Column('custrId',db.Integer(),db.ForeignKey('customer.cust_id'),unique=False,primary_key=True),
                  db.Column('adrsId',db.Integer(),db.ForeignKey('address.adr_id'),unique=False,primary_key=True))


class Address(db.Model):
    adrId = db.Column('adr_id',db.Integer(),primary_key=True)
    adrAname = db.Column('adr_aname', db.String(100))
    adrCity = db.Column('adr_city',db.String(100))
    adrState = db.Column('adr_state',db.String(100))
    adrPincode = db.Column('adr_pin',db.Integer())
    adrLandmark = db.Column('adr_landmark', db.String(100))
    ownAdrs = db.relationship('Owner', secondary=ownerAdrs, lazy='subquery', backref=db.backref('own_adrs', lazy=True))
    custrAdrs = db.relationship('Customer', secondary=custAdrs, lazy='subquery', backref=db.backref('cust_adrs', lazy=True))
