This module is heavily under development.
----------------------------------------
----------------------------------------


+ In future we may be providing setup tools to automatically install this module on local system


Installation Instruction / Usage
--------------------------------

+ for now this moudle has no dependencies other than tornado.
  you can install tornado by running below command

         pip install tornado
         
         
+ clone this project.

+ cd to the folder where web.py is located cd cqrs.io/ecommerce_cqrs_skeleton

+ run the below command.

        python web.py

  this will start tornado web server on 8888 port on your localhost.
  
+ to see admin panel browse to http://localhost:8888/admin
  below is the user credintial:
        ecommerce/cqrs
        
  you will see the list of product
  
  
+ to see the frontend browse to http://localhost:8888



Checking websocket/realtime functionality
-----------------------------------------
open frontend in more than one window and try to add product from admin panel, you will see product is also added on all open frontend/client.



TODO:
-----
+ use zmq queue and workers to insert product in to sqlite3.







