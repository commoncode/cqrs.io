This module is heavily under development.
----------------------------------------
----------------------------------------


Installation Instruction / Usage
--------------------------------

+ clone this project.

+ run
    setup.py

+ cd to the folder where web.py is located
    cd cqrs.io/ecommerce_cqrs_skeleton

+ run the below command.

        python web.py

  this will start tornado web server on 8888 port on your localhost.
  
+ start the publisher in another terminal
    
    python product_publisher.py
  
+ to see admin panel browse to http://localhost:8888/admin
  below is the user credintial:
        ecommerce/cqrs
        
  you will see the list of product
  
  
+ to see the frontend browse to http://localhost:8888



Checking websocket/realtime functionality
-----------------------------------------
open frontend in more than one window and try to add product from admin panel, you will see product is also added on all open frontend/client.








