from app import db

class Survivors(db.model):
    __tablename__ = 'survivors'
    __table_args__ = {'sqlite_autoincrement':True} #ja
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    gender = db.Column(db.String(20))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)

def __init__(self, name, gender, lat, lon):
    self.name = name
    self.gender = gender
    self.lat = lat
    self.lon = lon
