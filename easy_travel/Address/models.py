from EasyToTravel.config import db

cust_adr=db.Table('cust_adr',
                  db.column('custId',db.Integer(),db.ForeignKey('Customer.cust_id'),unique=False,primary_key=True),
                  db.column('adrId',db.Integer(),db.ForeignKey('Address.adr_id'),unique=False,primary_key=True))

class Address(db.Model):
    adrId=db.Column('adr_id',db.Integer(),primary_key=True)
    adrAname = db.Column('adr_aname', db.String(100))
    adrCity=db.Column('adr_city',db.String(100))
    adrState=db.Column('adr_state',db.String(100))
    adrPincode=db.Column('adr_pin',db.Integer())
    adrLandmark = db.Column('adr_landmark', db.String(100))
    ownerId = db.Column('ownadr_id',db.ForeignKey('owner.owner_id'),unique=False,nullable=True)
