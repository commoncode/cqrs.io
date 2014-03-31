#!/usr/bin/env python

"""
Implementing CQRS real-time communication with clients
"""

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
from models.db import _execute


#import zmq and install zmq's event loop as part of tornado
import zmq
from zmq.eventloop import ioloop
from zmq.eventloop.zmqstream import ZMQStream
ioloop.install()

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


socket_connections = []

def setupZmqSubscriber():
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect('tcp://127.0.0.1:5000')
    s.setsockopt(zmq.SUBSCRIBE, "")

    stream = ZMQStream(s)
    def echo(product):
    	print "receiving message: %s" % product
        for socket in socket_connections:
            socket.write_message(product[0])
    stream.on_recv(echo)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/admin", AdminLoginHandler),
            (r"/admin/products", AdminProductDashboardHandler),
            (r"/admin/addproducts", AdminProductAddHandler),
        ]
        settings = dict(
            cookie_secret="a5sdgf57698jkbdslfk98e7348jbksjd344",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            # xsrf_cookies=True,
            login_url="/admin/",
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    """
    def get_login_url():
        return "/admin/"
    """
    pass
        

class MainHandler(BaseHandler):
    def get(self):
        query = ''' select * from product '''
        cursorobj = _execute(query)
        self.render("index.html", products=cursorobj.fetchall())




class AdminLoginHandler(BaseHandler):
    def get(self):
        try:
            errormessage = self.get_argument("error")
        except:
            errormessage = ""
        self.render("login.html", errormessage = errormessage)

    def check_permission(self, password, username):
        if username == "ecommerce" and password == "cqrs":
            return True
        return False

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        auth = self.check_permission(password, username)
        if auth:
            self.set_current_user(username)
            self.redirect(self.get_argument("next", u"/admin/products"))
        else:
            error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect")
            self.redirect(u"/admin" + error_msg)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")


            
class AdminProductDashboardHandler(BaseHandler):
    def get(self):
        query = ''' select * from product '''
        cursorobj = _execute(query)
        self.render("admin_dashboard.html", products=cursorobj.fetchall())



class AdminProductAddHandler(tornado.websocket.WebSocketHandler):
    
    waiters = set()
    cache = []
    cache_size = 200

    def allow_draft76(self):
        # for iOS 5.0 Safari
        return True

    def open(self):
        socket_connections.append(self)

    def on_close(self):
        socket_connections.remove(self)
    
    @classmethod
    def update_cache(cls, product):
        cls.cache.append(product)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]
    
    
    @classmethod
    def send_updates(cls, product):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(product)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, product):
        logging.info("got product %r", product)
        logging.info("sending to queue on push socket tcp://127.0.0.1:5557")
        
        context = zmq.Context()
        zmq_socket = context.socket(zmq.PUSH)
        zmq_socket.bind("tcp://127.0.0.1:5557")
        zmq_socket.send_json({'product': tornado.escape.json_decode(product)})


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    setupZmqSubscriber()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
