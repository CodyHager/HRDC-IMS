
from peewee import *
import datetime



db = SqliteDatabase('inventory.db')


class Product(Model):
    product_name = CharField()
    inventory = IntegerField(default=0)
    price = DecimalField(decimal_places=2, auto_round=True)
    unit_type = CharField(null = True)
    ideal_stock = IntegerField()
    image_path = CharField(null=True)
    last_updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


db.connect()
if not db.table_exists('product'):
    db.create_tables([Product])




def add_product(name, stock, price,unit_type, ideal_stock, image_path=None):
    product, created = Product.get_or_create(
        product_name=name,
        defaults={
            'inventory': stock,
            'price': price,
            'unit_type': unit_type,
            'ideal_stock': ideal_stock,
            'image_path': image_path
        }
    )
    return product

#TODO
def delete_product():
    pass


#TODO
def get_product(name):
    pass

#TODO
def update_stock(name, new_stock):
    pass

#TODO other update methods


if __name__ == "__main__":
    add_product("Toilet Paper", 5, 20.00, "rolls", 100, "images/tp.jpg")

db.close()