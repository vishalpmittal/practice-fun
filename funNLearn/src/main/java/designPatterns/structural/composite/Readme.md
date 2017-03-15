Concepts
================
	-  Components represent part or whole structure
	-  compose objects into tree structures
	-  Individual object treated as a Composite
	-  Same operations applied on individual and composites
	-  Examples:
		-  java.awt.component
		-  JSF widgets
		-  RESTful service GETs

Design
================
	-  Tree structured
	-  Component
	-  Leaf or Composite, same operations
	-  Composite knows about child objects
	-  Component, Leaf, Composite


Pitfalls
================
	-  can overly simplify system
	-  difficult to restrict
	-  Implementation can possibly be costly
	
Comparison
===============
	-  Composite
		-  tree structure
		-  Leaf and composite have same interface
		-  Unity between objects
	-  Decorator
		-  Contains another entity
		-  Modifies behavior(adds)
		-  Doesn't change underlying object
		