Products = new Meteor.Collection("products", {idGeneration:'MONGO'});
Cart = new Meteor.Collection("cart", {idGeneration:'MONGO'});
Operationslog = new Meteor.Collection("operationslog", {idGeneration:'MONGO'});

if (Meteor.isClient) {
  Meteor.subscribe("products");
  Meteor.subscribe("cart");
  Meteor.subscribe("operations");
  
  Template.productlist.products = function() {
      return Products.find();
  };
  
  Template.cartlist.cproducts = function() {
      return Cart.find({owner:Meteor.userId()});
  };
  
  Template.operationlog.cqrslog = function() {
      return Operationslog.find();
  };
  

  
  Template.product.events({
      'click .btnAddToCart': function() {
          if(Cart.find({name:this.name}).count() == 0) {
              Operationslog.insert({description:"Add to cart for product : " + this.name, productname: this.name, status: "Initiated", userid: Meteor.userId()});
              Cart.insert({name:this.name, owner: Meteor.userId()});
              //Operations.update({productname:this.name, userid: Meteor.userId()}, { $set: { status: "Complete" } });
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
