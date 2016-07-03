from app import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(255), unique=True)
    country = db.Column(db.String(255))
    password_hash = db.Column(db.String(128))
    reviews = db.relationship('Review', backref='user_ref', lazy='dynamic')

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(200), index=True, unique=True)
    product_model = db.Column(db.String(200), index=True, unique=True)
    processor = db.Column(db.String(300), index=True, unique=True)
    display = db.Column(db.Integer, index=True, unique=True)
    ram_memory = db.Column(db.String(200), index=True, unique=True)
    memory_speed = db.Column(db.Integer, index=True, unique=True)
    hard_drive = db.Column(db.Integer, index=True, unique=True)
    video_card = db.Column(db.String(200), index=True, unique=True)
    card_description = db.Column(db.String(100), index=True, unique=True)
    battery_life = db.Column(db.Integer, index=True, unique=True)
    item_weight = db.Column(db.Integer, index=True, unique=True)
    housing_material = db.Column(db.String(100), index=True, unique=True)
    color = db.Column(db.String(100), index=True, unique=True)
    operating_system = db.Column(db.String(100), index=True, unique=True)
    reviews = db.relationship('Review', backref='product_ref', lazy='dynamic')

    def __repr__(self):
        return '<Product %r>' % (self.product_model)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    opinions = db.relationship('Opinion', backref='review_ref', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Review %r>' % (self.body)

class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    aspect = db.Column(db.String)
    attribute = db.Column(db.String)
    emotion = db.Column(db.String)
    polarity = db.Column(db.String)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'))

    def __repr__(self):
        return '<Opinion %r>' % (self.body)
