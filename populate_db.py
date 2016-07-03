from app import db, models
import datetime
import parse_romanian
products = parse_romanian.getProducts('Laptops_romanian.xml')
print(products)

# usernames = []
# for product in products:
#     (brand, model, processor, display, ram_memory, memory_speed, hard_drive, video_card, card_description, battery_life, item_weight, housing_material, color, operating_system) = product['info']
#     reviews = product['reviews']
#     p = models.Product(brand=brand, product_model=model, processor = processor, display = display, ram_memory= ram_memory,
#                           memory_speed = memory_speed , hard_drive = hard_drive, video_card = video_card,
#                           card_description = card_description, battery_life = battery_life, item_weight = item_weight,
#                           housing_material = housing_material, color = color, operating_system = operating_system)
#     db.session.add(p)
#     for (reviewUser, reviewText, sentences) in reviews:
#         if not reviewUser in usernames:
#             u = models.User(username=reviewUser)
#             usernames.append(reviewUser)
#             db.session.add(u)
#         r = models.Review(body=reviewText, timestamp=datetime.datetime.utcnow(), product_ref=p, user_ref = u)
#         db.session.add(r)
#         for (sentenceText, aspect, attribute, emotion, polarity) in sentences:
#              s = models.Opinion(body=sentenceText, aspect=aspect, attribute=attribute, emotion=emotion, polarity=polarity, review_ref=r)
#              db.session.add(s)
#     db.session.commit()

# products = models.Product.query.all()
# # print(products)
# for p in products:
#     # print(p.id,p.product_model)
#     reviews = p.reviews.all()
#     for r in reviews:
#         print(r)
#         opinions = r.opinions.all()
#         print(opinions)
#     # print(reviews)
#
# users = models.User.query.all()
# for user in users:
#     if user.username == 'realuser1':
#         my_user_id = user.id
#
# reviews = models.Review.query.all()
# for review in reviews:
#     if review.user_id == my_user_id:
#         print(review)

# p = models.Product.query.get(1)
# print(p.product_model)
# reviews = p.reviews.all()
# print(reviews)

# clear database
# opinions = models.Opinion.query.all()
# for opinion in opinions:
#     db.session.delete(opinion)
#
# users = models.User.query.all()
# for user in users:
#     db.session.delete(user)
#
# reviews = models.Review.query.all()
# for review in reviews:
#     db.session.delete(review)
#
# products = models.Product.query.all()
# for p in products:
#     db.session.delete(p)
# db.session.commit()