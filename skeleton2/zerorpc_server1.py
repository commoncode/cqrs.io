import zerorpc
import json

from mongoengine import *

connect("meteor", host="mongodb://127.0.0.1:3001/meteor")



class Cart(Document):
    name = StringField()
    owner = StringField()
    
class Oplogqueue(Document):
    description = StringField()
    productname = StringField()
    status = StringField()
    userid = StringField()
    

class EcommerceRPC1(object):
    def save_product_to_cart(self, cart):
        print "Saving Product to Cart"
        print cart
        cart_obj = json.loads(cart)
        print cart_obj
        
        ''' Operation queue starts '''
        print "Saving oplogqueue"
        product_oplogqueue = Oplogqueue(description="Add to Cart for product '" + cart_obj["name"] + "'", productname=cart_obj["name"], status="Initiated", userid=cart_obj["owner"])
        product_oplogqueue.save()
        print "Oplogqueue Saved"
        ''' Operation queue ends '''
        
        cart_mongo = Cart(name=cart_obj["name"], owner=cart_obj["owner"])
        print cart_mongo
        cart_mongo.save()
        
        ''' Operation queue starts '''
        # product_oplogqueue.status="Complete"
        # product_oplogqueue.save()
        ''' Operation queue ends '''
        
        return "Product saved to Cart"
        
        
s = zerorpc.Server(EcommerceRPC1())
s.bind("tcp://0.0.0.0:4243")
s.run()
