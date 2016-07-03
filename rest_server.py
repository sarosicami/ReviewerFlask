from flask import Flask, jsonify, abort, request, make_response, url_for, g
from app import db, models
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import update
import datetime
import extract
import parse_romanian
import trainRomanian
import testRomanian

app = Flask(__name__)
app.config.from_object('config')
auth = HTTPBasicAuth()

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/reviewer/api/users', methods = ['POST'])
def new_user():
    print('new user')
    username = request.json.get('username')
    print(username)
    password = request.json.get('password')
    email = request.json.get('email')
    country = request.json.get('country')
    if models.User.query.filter_by(username = username).first() is not None:
        return jsonify({'error': 'The username already exists'}) # existing user
    else:
        user = models.User(username = username, email = email, country = country)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'error': '', 'username': user.username, 'email': user.email, 'country': user.country}), 201, {'Location': url_for('get_user', id = user.id, _external = True)}

@app.route('/reviewer/api/login', methods = ['POST'])
def login_user():
    username = request.json.get('username')
    password = request.json.get('password')
    user = models.User.query.filter_by(username = username).first()
    if not user:
        return jsonify({'error': 'Please verify your username'})
    elif not user.verify_password(password):
        return jsonify({'error': 'Username and password do not match'})
    else: return jsonify({'error':'', 'id': user.id, 'username': user.username, 'email': user.email, 'country': user.country}), 201, {'Location': url_for('get_user', id = user.id, _external = True)}

@app.route('/reviewer/api/users/<int:id>')
def get_user(id):
    user = models.User.query.get(id)
    if not user:
        abort(400)
    return jsonify({ 'username': user.username, 'email': user.email, 'country': user.country})

@auth.verify_password
def verify_password(username, password):
    user = models.User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

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
            'processor': p.processor,
            'display': p.display,
            'ram_memory': p.ram_memory,
            'memory_speed': p.memory_speed,
            'hard_drive': p.hard_drive,
            'video_card': p.video_card,
            'card_description': p.card_description,
            'battery_life': p.battery_life,
            'item_weight': p.item_weight,
            'housing_material': p.housing_material,
            'color': p.color,
            'operating_system': p.operating_system,
        }
        new_products.append(product_dict)
    return new_products

def reviews_dict_list(reviews):
    # print(reviews)
    new_reviews = []
    id = 0
    for r in reviews:
        id += 1
        review_dict = {
            'id': id,
            'body': r.body,
            'timestamp': r.timestamp,
            'product_id': r.product_id,
            'user_id':r.user_id
        }
        new_reviews.append(review_dict)
    return new_reviews

def opinions_dict_list(opinions_list):
    # print(opinions)
    new_opinions = []
    id = 0
    for op_list in opinions_list:
        for op in op_list:
            id += 1
            opinion_dict = {
                'id': id,
                'body': op.body,
                'aspect': op.aspect,
                'attribute': op.attribute,
                'emotion': op.emotion,
                'polarity': op.polarity,
                'review_id': op.review_id,
            }
            new_opinions.append(opinion_dict)
    return new_opinions


@app.route('/reviewer/api/products', methods=['GET'])
# @auth.login_required
def get_products():
    # return jsonify({'products': [make_public_product(product) for product in products]})
    products_list = products_dict_list()
    return jsonify({'products': products_list})

@app.route('/reviewer/api/product/<int:product_id>', methods=['GET'])
# @auth.login_required
def get_product(product_id):
    product = [product for product in products_dict_list() if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    return jsonify({'product': product[0]})

@app.route('/reviewer/api/reviews/<int:product_id>', methods=['GET'])
def get_product_reviews(product_id):
    product = models.Product.query.get(product_id)
    reviews = reviews_dict_list(product.reviews.all())
    return jsonify({'reviews': reviews})

@app.route('/reviewer/api/opinions/<int:review_id>', methods=['GET'])
# @auth.login_required
def get_review_opinions(review_id):
    review = models.Review.query.get(review_id)
    opinions = opinions_dict_list(review.opinions.all())
    return jsonify({'opinions': opinions})

@app.route('/reviewer/api/all_opinions/<int:product_id>', methods=['GET'])
# @auth.login_required
def get_reviews_all_opinions(product_id):
    product = models.Product.query.get(product_id)
    reviews = product.reviews.all()
    all_opinions = []
    for review in reviews:
        review_db = models.Review.query.get(review.id)
        all_opinions.append(review_db.opinions.all())
    opinions = opinions_dict_list(all_opinions)
    return jsonify({'opinions': opinions})

@app.route('/reviewer/api/new_review/opinions', methods=['POST'])
# @auth.login_required
def get_new_review_opinions():
    user_id = int(request.json.get('user_id'))
    product_id = int(request.json.get('product_id'))
    reviewText = request.json.get('review_text')
    test_reviews = extract.split_review_based_on_punctuation(reviewText)

    aspect_result = testRomanian.reviewsAspectData(test_reviews)
    print(aspect_result)
    attribute_result = testRomanian.reviewsAttributeData(test_reviews)
    print(attribute_result)
    polarity_result = testRomanian.reviewsPolarityData(test_reviews)
    print(polarity_result)
    emotion_result = testRomanian.reviewsEmotionData(test_reviews)
    print(emotion_result)

    opinions = []
    for i in range(0, len(test_reviews)):
        opinion_dict = {
                    'body': test_reviews[i],
                    'aspect': aspect_result[i],
                    'attribute': attribute_result[i],
                    'emotion': emotion_result[i],
                    'polarity': polarity_result[i],
                }
        opinions.append(opinion_dict)
    print(opinions)
    return jsonify({'opinions': opinions})

@app.route('/reviewer/api/add_review', methods = ['POST'])
def new_review():
    print('new review')
    user_id = int(request.json.get('user_id'))
    print(user_id)
    product_id = int(request.json.get('product_id'))
    reviewText = request.json.get('review_text')
    if user_id <= 0 or product_id <= 0 or reviewText is None:
        abort(400) # missing arguments
    if models.Review.query.filter_by(body = reviewText, user_id = user_id).first() is not None:
        return jsonify({'error': 'This review was already registered'}) # existing user
    else:
        p = models.Product.query.get(product_id)
        u = models.User.query.get(user_id)
        r = models.Review(body=reviewText, timestamp=datetime.datetime.utcnow(), product_ref=p, user_ref = u)
        db.session.add(r)

        reviewText = request.json.get('review_text')
        test_reviews = extract.split_review_based_on_punctuation(reviewText)
        aspect_result = testRomanian.reviewsAspectData(test_reviews)

        print(aspect_result)
        attribute_result = testRomanian.reviewsAttributeData(test_reviews)
        print(attribute_result)
        polarity_result = testRomanian.reviewsPolarityData(test_reviews)
        print(polarity_result)
        emotion_result = testRomanian.reviewsEmotionData(test_reviews)
        print(emotion_result)

        # return jsonify({'result': result})
        opinions = []
        for i in range(0, len(test_reviews)):
            s = models.Opinion(body=test_reviews[i], aspect=aspect_result[i], attribute=attribute_result[i], emotion=emotion_result[i], polarity=polarity_result[i], review_ref=r)
            db.session.add(s)
        db.session.commit()

        all_review_opinions = []
        all_review_opinions.append(r.opinions.all())
        opinions = opinions_dict_list(all_review_opinions)
        print(opinions)
        return jsonify({'error':'','opinions': opinions})

if __name__ == '__main__':
    app.run(debug=True)