from EasyToTravel.config import db
from EasyToTravel.easy_travel.Owner.ownercontroller import *
from EasyToTravel.easy_travel.Driver.drivercontroller import *
from EasyToTravel.easy_travel.Customer.custcontroller import *
from EasyToTravel.easy_travel.Address.adrcontroller import *
from EasyToTravel.easy_travel.Vehicle.vehiclecontroller import *
from EasyToTravel.easy_travel.Payment.paymentcontroller import *
from EasyToTravel.easy_travel.Trips.tripscontroller import *
from EasyToTravel.easy_travel.Notifications.notificationcontroller import *
from EasyToTravel.easy_travel.History.historycontroller import *

db.create_all()
print('Table Created')