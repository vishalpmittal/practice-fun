Creational
--------------------
	- Singleton: restricts the instantiation of a class to one object
	- Builder: uses another object, a builder to resolve "The telescoping constructor anti-pattern
	-  Prototype :  It is used when the type of objects to create is determined by a prototypical instance, which is cloned to produce new objects. avoid the inherent cost of creating a new object in the standard way 
	- Factory Method : uses factory methods to deal with the problem of creating objects without having to specify the exact class of the object that will be created. 
	- Abstract Factory:  The client doesn't know (or care) which concrete objects it gets from each of these internal factories, since it uses only the generic interfaces of their products.[1] This pattern separates the details of implementation of a set of objects from their general usage and relies on object composition, as object creation is implemented in methods exposed in the factory interface.
	
Structural
--------------------
	- Adapter: allows the interface of an existing class to be used from another interface. used to make existing classes work with others without modifying their source code.
	- Bridge: decouple an abstraction from its implementation so that the two can vary independently
	- Composite : a group of objects is to be treated in the same way as a single instance of an object.
	- Decorator: allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class
	- Facade: 
		-  make a software library easier to use, understand and test, since the facade has convenient methods for common tasks
		-  make the library more readable, for the same reason
		-  reduce dependencies of outside code on the inner workings of a library, since most code uses the facade, thus allowing more flexibility in developing the system
		-  wrap a poorly designed collection of APIs with a single well-designed API.
		
	- Flyweight: minimizes memory use by sharing as much data as possible with other similar objects
	- Proxy: 