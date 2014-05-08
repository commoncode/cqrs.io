Install Meteor:
----------------

    curl https://install.meteor.com | /bin/sh
    
    cd meteorapp
    
    meteor add accounts-password
    
    meteor add accounts-ui
    
    meteor add http
    
    meteor
    

On the meteor frontend now you can see the shopping cart and operation log section, you can add product to cart (only logedin user can do so).
adding product to cart action consumes a DRF rest api to add product to cart, and operations logs are shown in the operations logs section.
    
###Thats all!

