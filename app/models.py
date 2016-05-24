from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(200), index=True, unique=True)
    product_model = db.Column(db.String(200), index=True, unique=True)
    model_number = db.Column(db.String(200), index=True, unique=True)
    processor = db.Column(db.String(300), index=True, unique=True)
    display = db.Column(db.Integer, index=True, unique=True)
    RAM_memory = db.Column(db.String(200), index=True, unique=True)
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

    def __repr__(self):
        return '<Review %r>' % (self.body)
