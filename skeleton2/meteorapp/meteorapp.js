Products = new Meteor.Collection("products", {idGeneration:'MONGO'});
Cart = new Meteor.Collection("cart", {idGeneration:'MONGO'});
Oplogqueue = new Meteor.Collection("oplogqueue", {idGeneration:'MONGO'});

if (Meteor.isClient) {
  Meteor.subscribe("products");
  Meteor.subscribe("cart");
  Meteor.subscribe("oplogqueue");
  
  Template.productlist.products = function() {
      return Products.find();
  };
  
  Template.cartlist.cproducts = function() {
      return Cart.find({owner:Meteor.userId()});
  };
  
  Template.oplogqueue.cqrslogs = function() {
      return Oplogqueue.find({userid: Meteor.userId()});
  };
  
  Template.cqrslog.statusIsInitiated = function(status) {
      return this.status == "Initiated"
          
  };
  
  Template.cqrslog.statusIsCompleted = function(status) {
      return this.status == "Complete"
  };
  
  Template.product.events({
      'click .btnAddToCart': function() {
          var op_id = null;
          if(Cart.find({name:this.name, owner: Meteor.userId()}).count() == 0) {
              /*
              op_id = Oplogqueue.insert({description:"Add to cart for product : " + this.name, productname: this.name, status: "Initiated", userid: Meteor.userId()});
              Cart.insert({name:this.name, owner: Meteor.userId()});
              Oplogqueue.update({_id:op_id}, { $set: { status: "Complete" } });
              */
              HTTP.call(
                "post", "http://localhost:8000/cart/",
                {
                    params: {name:this.name, owner: Meteor.userId()},
                    headers: {"Content-Type":"application/x-www-form-urlencoded", "Accept":"application/json"}
                },
                function(error, result) {
                    console.log(error);
                    console.log(result);
              });
              
          } else {
              alert("already in cart");
          }
      }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
      
    // code to run on server at startup
    /*
    if(Products.find().count() === 0) {
        var products = [
            {
                name: "Mobile",
                description: "A Slim Mobile phone",
                price: "400"
            },
            {
                name: "Charger",
                description: "A thin Charger for Mobile phone",
                price: "500"
            }
        ];
        
        for(var i = 0; i < products.length; i++) {
            Products.insert({name: products[i].name, description: products[i].description, price: products[i].price});
        }
    }
    */
  });
}
