Builder Pattern

-  Handles complex constructors
-  Large number of parameters
-  Immutability
Eg:
     -  StringBuilder
     -  DocumentBuilder  
  -  Locale.Builder

Design
-  Flexibility over telescoping constructors
-  Static inner class
-  Class appropriate constructor
-  Negates the need for exposed setters
-  Java 1.5+ can take advantage of Generics


-  Pitfalls
  -  Immutable
  -  Inner Static class
  -  Designed first
  -  Complexity

-  Builder vs. Prototype
  -  Builder Pattern
     -  Handles complex constructors
     -  No interface required
     -  can be a separate class
     -  works with legacy code
  
  -  Prototype Pattern
     -  Implemented around a clone
     -  Avoids calling complex constructors
     -  Difficult to implement in legacy
