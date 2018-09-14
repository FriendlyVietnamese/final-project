from mongoengine import *

class Trasua(Document):
    name = StringField()
    sugar = StringField()
    ice = StringField()
    size = StringField()
    topping = StringField()

class User(Document):
    surname = StringField()
    fullname = StringField()
    username = StringField()
    email = EmailField()
    password = StringField()
    phone = StringField()
    address = StringField()
    trasua_id = ListField(ReferenceField(Trasua))


# trasua = Trasua(
#     name = StringField()
#     sugar = StringField()
#     ice = StringField()
#     size = StringField()
#     topping = StringField()
# )
# trasua.save()

# form = request.form
# name = form['name']
# age = form['age']

# vlinh = User(
#     name = name,
#     age = age,
#     ...
#     trasua_id = []
# )
# vlinh.save()

# vlinh.update(push__trasua_id = trasua)
