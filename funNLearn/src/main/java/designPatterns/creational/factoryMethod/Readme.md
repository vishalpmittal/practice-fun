Factory Method Pattern
---------------------------------------------
-  Opposite to singleton method
-  Doesn't expose instantiation logic
-  Defer to subclasses
-  Common interface
-  Specified by architecture, implemented by user
-  pre existing java eg: 
	-  Calendar
	-  ResourceBundle
	-  NumberFormat

-  Pit falls
	-  Complex. 
	-  Creation happens in the subclasses
	-  design at the beginning and can not be refactored 

Comparison with others	

	Singleton
	-  Returns same instance
		-  One constructor method - no args
	-  No interface
	-  No subclasses
	Factory
	-  Returns various instances
		-  Multiple constructors
	-  Interface driven
	-  Subclasses
	-  Adaptable to environment more easily
	