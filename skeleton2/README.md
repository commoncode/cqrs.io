This project is in progress, Not intended to use in production:
---------------------------------------------------------------


Install
-------
[meteorapp](https://github.com/commoncode/cqrs.io/tree/master/skeleton2/meteorapp)
    
[djangoadmin](https://github.com/commoncode/cqrs.io/tree/master/skeleton2/djangoadmin)
    


Usage
-----

Make sure meteorapp and djangoadmin are running

Start the ZeroRPC Server
    
    python zerorpc_server.py
    
    python zerorpc_server1.py
    

check by adding product from django admin you will see those products added on meteorapp frontend.

Behind the scene
----------------

1. product added from djangoadmin
2. django admin adds product to RDBMS/Sqlite and send it to zerorpc_server on wire
3. zerorpc_server adds product to mongodb, where meteorapp is listening to mongodb, as soon as mongodb gets updates its published to all open meteorapp clients.

###Thats all!




