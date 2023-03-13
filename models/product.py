from main import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    categary = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    live = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.Float, nullable=False)
    owner = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)
    bid_by = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=True)
    winner = db.Column(db.String(100), nullable=True)