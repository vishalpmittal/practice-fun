Prototype Pattern

-  Avoids new keywords i.e. costly creations
-  Avoids subclassing
-  Usually implemented with a Registry
-  uses cloning concepts to create new objects
-  typically implements clone() or clonable() method

-  Shallow copy
	Create a clone of top level object but use the same references for any objects referenced inside of the top level object

-  Deep Copy
	create clone of even the internally referenced objects 

-  Pitfalls
  -  Not clear when to use
  -  Usually used with other patterns
  -  does a shallow copy but usually we need a deep copy

-  Prototype vs. Factory pattern
  -  Prototype
    -  lighter weight construction
    -  shallow or deep
    -  copy of itself
  -  Factory
    -  Flexible Objects (Multiple constructors)
    -  Concrete Instance
    -  Fresh Instance
