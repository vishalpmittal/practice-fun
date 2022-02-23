# Spring Boot 

https://start.spring.io/



### Annotations
---------------
* @SpringBootApplication : used in main class or bootstrap class 
* @EnableAutoConfiguration: 

* Custom Endpoint
  - @Endpoint 
  - @WebEndpointer
  - @WebEndpointExtension

* @RequestMapping
  - Provide the routing information
* @RestController
  - 

### Properties
--------------
* server.http2.enabled=true
* spring.datasource.url = jdbc:mysql://localhost:3306/example
* spring.datasource.username=root
* spring.datasource.password=mysql
* spring.jpa.hibernate.ddl-auto=create-drop
  - The values create, create-drop, validate, and update basically influence how the schema tool management will manipulate the database schema at startup.


### JPA (Java Persistence API) vs. Hibernate:
* JPA : Data access abstraction used to reduce the amount of boilerplate code 
* Hibernate: implementation of JPA


### spring boot CLI
```groovy
@RestController public class Sample {
    @RequestMapping ("/example")
    String index(){
        <h1>"Hello World!"</h1>;
    }
}
```

```bash
./spring run Sample.groovy
```

### Profiles: 
---------------
- provides a way to segregate the parts of the application configuration and make it available in environment
- eg. dev, prod, test, sandbox related config
- use argument: -Dspring.profiles.active=prod
- in application.properties file use: spring.profiles.active=prod


### Deployment
--------------
* Option 1: generate a jar using maven artifacts and run 
* Option 2: Generate a war file and deploy that using a favorite web server (tomcat, jetty, jersey, etc.)

### Advantages
--------------
Stability, Based on JVM, Connectivity, Cloud-Native, Flexibility, Open Source

### Features
------------
* Auto-dependency resolution and Starter dependency 
* Embedded HTTP servers
* Auto-configuration
  - if you have a data source bean present in the classpath of the application, it automatically configures JDBC template
* management endpoints
* Spring Boot CLI
* Spring Initializer 
* Spring Actuator
* Logging and Security

### Spring vs Spring Boot
--------------
* Spring is web-app framework while spring boot is a module of spring
