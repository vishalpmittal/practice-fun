Concepts
==========
	-  Make an API easier to use
	-  Reduce dependencies on outside code
	-  Simplify the interface or client usage
	-  Usually a refactoring pattern
	-  Examples:
		java.net.URL
		javax.faces.context.FacesContext

Design
=========
	-  Class that utilizes composition
	-  shouldn't have a need for inheritance
	-  Typically encompasses full life cycle

Pitfalls
=========
	-  Typically used to clean up code
	-  Should thing about API design
	-  Flat problem/structure
	-  The singleton of structural pattern

Comparison
=========
	-  Facade
		-  Simplifies interface
		-  works with composites
		-  cleaner apis
		
	-  Adapter
		-  Also a refectoring pattern
		-  Modifies behavior (adds)
		-  Provides a different interface
		