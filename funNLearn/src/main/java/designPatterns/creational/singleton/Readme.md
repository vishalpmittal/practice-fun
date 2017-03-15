Singleton Pattern
-  Only one instance created
-  Guarantees control of a resource
-  lazily loaded
Eg.
     -  Runtime
     -  Logger
     -  Spring Beans
     -  Graphic Managers

Design:
-     Class is reponsible for lifecycle
-     Static in nature
-     Needs to be thread safe
-     Private instance
-     Private constructor
-     No parameters required for construction


Singleton vs. Factory are contrasts
-  Singleton
     -  Returns same instance
     -  One constructor method - no args
     -  no Interface
-  Factory
     -  Returns various instances
     -  multiple constructors 
     -  interface driven
     -  Adaptable to environment more easily

Pitfalls
-  often overused
-  Difficult to unit test
-  if not careful, not thread safe
-  sometimes confused for Factory
-  java.util.Calendar is NOT a Singleton
