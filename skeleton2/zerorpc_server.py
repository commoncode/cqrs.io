import zerorpc
import json

from mongoengine import *

connect("meteor", host="mongodb://127.0.0.1:3001/meteor")



class Products(Document):
    name = StringField()
    description = StringField()
    price = StringField()
    
class Cart(Document):
    name = StringField()
    owner = StringField()
    
class Oplogqueue(Document):
    description = StringField()
    productname = StringField()
    status = StringField()
    userid = StringField()
    

class EcommerceRPC(object):
    def save_product(self, product):
        print "Saving product"
        print product
        product_obj = json.loads(product)
        print product_obj
        product_mongo = Products(name=product_obj["name"], description=product_obj["description"], price=product_obj["price"])
        print product_mongo
        product_mongo.save()
        return "Product saved"
        
s = zerorpc.Server(EcommerceRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
