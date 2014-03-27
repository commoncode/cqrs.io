$(document).ready(function() {
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};
    
    
    
    $("#btnAddNewProduct").click(function() {
        //console.log("clicked");
        $("#frmAddNewProduct").slideToggle("slow");
    });

    
    $("#frmAddNewProduct").submit(function() {
        newProduct($(this));
        return false;
    });
    $("#frmAddNewProduct").keypress(function(e) {
        if (e.keyCode == 13) {
            newProduct($(this));
            return false;
        }
    });
    
    updater.start();
});

function newProduct(form) {
    var product = form.formToDict();
    updater.socket.send(JSON.stringify(product));
    
}

jQuery.fn.formToDict = function() {
    var fields = this.serializeArray();
    var json = {}
    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

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
        var node = $(product.html);
        node.hide();
        $("#tblProduct tbody").append(node);
        node.slideDown();
    }
};
