$(document).ready(function() {
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};
    
    updater.start();
});

var updater = {
    socket: null,

    start: function() {
        var url = "ws://" + location.host + "/admin/addproducts";
	updater.socket = new WebSocket(url);
	updater.socket.onmessage = function(event) {
	    updater.showProduct(JSON.parse(event.data));
	}
    },

    showProduct: function(product) {
        console.log(product);
        var existing = $("#p" + product.id);
        if (existing.length > 0) return;
        var node = $(['<section id="p', product.id, '"><ul><li><strong>Item Id :</strong> #P', product.id, '</li><li><strong>Name :</strong> ', product.name, '</li><li><strong>Description :</strong> ', product.description, '</li><li><strong>Price :</strong> $ ', product.price, '</li></ul>        </section>'].join(''));
        node.hide();
        $(".productList").append(node);
        node.slideDown();
    }
};
