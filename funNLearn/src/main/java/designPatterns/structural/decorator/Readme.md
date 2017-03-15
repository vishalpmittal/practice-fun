Concepts
==========
	-  also called a wrapper
	-  add behavior without affecting others
	-  more than just inheritance
	-  single responsibility principle (class should do one thing and do it well)
	-  compose behavior dynamically
	-  eg:
		java.io.InputStream
		java.util.Collections#checkedList
		UI components in AWT

Design
=========
	-  Inheritance based
	-  Utilizes composition and inheritances (is-a, has-a)
	-  alternative to subclassing
	-  Constructor requires instance from hierarchy
	
Pitfalls
=========
	-  New class for every feature added
	-  Multiple little objects
	-  Often confused with simple inheritance
	
Contrast
===========
	-  Composite
		-  tree structure
		-  Leaf and composite have same interface
		-  Unity between objects
	-  Decorator
		-  Contains another entity
		-  Modifies behavior(adds)
		-  Doesn't change underlying object