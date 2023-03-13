from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name