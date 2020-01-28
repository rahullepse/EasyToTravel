from EasyToTravel.config import db

class Notification(db.Model):
    notfyId = db.Column('notfy_id',db.Integer(),primary_key=True)
    notfyMsg = db.Column('notfy_msg',db.String(200))

