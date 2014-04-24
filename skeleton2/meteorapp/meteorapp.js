Products = new Meteor.Collection("products", {idGeneration:'MONGO'});

if (Meteor.isClient) {
  Meteor.subscribe("products");
  Template.productlist.products = function() {
      return Products.find();
  };
  
  /*
  Template.hello.greeting = function () {
    return "Welcome to meteorapp.";
  };

  Template.hello.events({
    'click input': function () {
      // template data, if any, is available in 'this'
      if (typeof console !== 'undefined')
        console.log("You pressed the button");
    }
  });
  */
  
  Template.product.events({
      'click .btnAddToCart': function() {
          console.log(this);
      }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
    if(Products.find().count() === 0) {
        var products = [
            {
                name: "Mobile",
                description: "A Slim Mobile phone",
                price: "$ 400"
            },
            {
                name: "Charger",
                description: "A thin Charger for Mobile phone",
                price: "$ 500"
            }
        ];
        
        for(var i = 0; i < products.length; i++) {
            Products.insert({name: products[i].name, description: products[i].description, price: products[i].price});
        }
    }
  });
}
