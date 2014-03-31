import zmq
import time
from random import choice
from models.db import _execute

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5000")

context1 = zmq.Context()
consumer_receiver = context.socket(zmq.PULL)
consumer_receiver.connect("tcp://127.0.0.1:5557")
 
while True:
    parsed = consumer_receiver.recv_json()["product"]
    
    query = ''' INSERT INTO product (name, description, price) VALUES('%s','%s',%s)''' % (parsed["productname"], parsed["productdescription"], parsed["productprice"])
    
    cursorobj = _execute(query)
    productId = cursorobj.lastrowid
    query = ''' SELECT * from product where id=%s''' % (productId)
    cursorobj = _execute(query)
    row = cursorobj.fetchone()
    product = {}
    product["id"] = row[0]
    product["name"] = row[1]
    product["description"] = row[2]
    product["price"] = row[3]
    
    print "-> %r",product
    socket.send_json( product )
    time.sleep(.1)
