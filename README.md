cqrs.io
=======

Common Code is looking to create a Realtime / Event loop based messaging system to assist the functioning of CQRS systems implemented in Python / Django & JS / Node / Meteor.

It's expected, however, that the system may include other language implementations.


CQRS
----

CQRS is an architecture that separates the Write DB to the Read DB; amongst other assumptions; in order to create performant systems.


Objectives
----------

The early objectives of the system are:

+ provide a Client system realtime messaging on events pertaining to the update / writing of data on the Command/Server side of the architecture

For example:

+ We have a Django managed RDBMs with Polymorphic models supporting business logic.
+ There is a REST or RPC API that the client, Meteor / Node, "Read" side – requests an update, say "add a product to cart"
+ Because there are several operations that the Django side must perform, i.e.:
  + Put the task in a queue | Write to the DB | Trigger the signal to serialize | Serialize all the relevant Document collections
+ We want to "inform" the client system on the stages of progress.


Other Objectives
----------------

+ There will be other Verbs and Responses that we might create; discuss what these might be.


Technologies
------------

The following technologies are interesting:

+ zerorpc
+ Meteor's DDP (Dynamic Data Protocol)
  + See also python implemented DDP clients
+ Tornado
+ GEvent
+ CQRS
+ JSON / MessagePack / 0MQ


Other Comments
--------------

+ "In someways, this might turn out to be a sort of DDP Server written in Python"
+ "... it'll be interesting to create a distributed realtime protocol to support the business logic of our solutions."
+ "... Common Code is interested in creating systems that are more Statefull... this idea seems to support that... and as an alternative to the Request / Response metaphor that HTTP has given us"

