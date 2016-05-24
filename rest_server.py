from flask import Flask, jsonify, abort, request, make_response, url_for
from app import db, models

app = Flask(__name__)
app.config.from_object('config')

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

def make_public_product(product):
    new_product = {}
    for field in product:
        if field == 'id':
            new_product['uri'] = url_for('get_product', product_id = product['id'], _external = True)
        else:
            new_product[field] = product[field]
    return new_product

products = models.Product.query.all()

def products_dict_list():
    new_products = []
    id = 0
    for p in products:
        id += 1
        product_dict = {
            'id': id,
            'brand': p.brand,
            'product_model': p.product_model,
            'model_number': p.model_number,
            'processor': p.processor,
            'display': p.display,
            'RAM_memory': p.RAM_memory,
            'memory_speed': p.memory_speed,
            'hard_drive': p.hard_drive,
            'video_card': p.video_card,
            'card_description': p.card_description,
            'baterry_life': p.battery_life,
            'item_weight': p.item_weight,
            'housing_material': p.housing_material,
            'color': p.color,
            'operating_system': p.operating_system
        }
        new_products.append(product_dict)
    return new_products

def reviews_dict_list(reviews):
    print(reviews)
    new_reviews = []
    id = 0
    for r in reviews:
        id += 1
        review_dict = {
            'id': id,
            'body': r.body,
            'timestamp': r.timestamp,
            'product_id': r.product_id,
        }
        new_reviews.append(review_dict)
    return new_reviews

@app.route('/reviewer/api/products', methods=['GET'])
def get_products():
    # return jsonify({'products': [make_public_product(product) for product in products]})
    products_list = products_dict_list()
    return jsonify({'products': products_list})

@app.route('/reviewer/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products_dict_list() if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    return jsonify({'product': product[0]})

@app.route('/reviewer/api/reviews/<int:product_id>', methods=['GET'])
def get_product_reviews(product_id):
    print(product_id)
    product = models.Product.query.get(product_id)
    reviews = reviews_dict_list(product.reviews.all())
    return jsonify({'reviews': reviews})

if __name__ == '__main__':
    app.run(debug=True)