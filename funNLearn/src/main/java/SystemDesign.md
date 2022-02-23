## Architectures:
-----------------
* Monolithic, Microservices, Distributed

## SOLID (oops principle): 
--------------------------
  + Single Responsibility: 
  + Open/Closed : open for extension but closed for modifications
  + Liskov Substitution: derived types must be completely substitutable for their base types
  * Interface Segregation: Not be forced to implement unnecessary methods that are not used.
  * Dependency Inversion: depend on abstraction, not on concretion. In short Modularization

## Database Normalization (3NF)
-------------------------------
- do not replicate data
- use integer of keys
- add special key column to each table, which you will make reference to




## Characterstics of a good design:
-----------------------------------
* Features Coverage
* APIs definition
* Scalability
  + Horizontal scaling : distributed system
  + Vertical scaling : add more CPU RAM storage etc.
* Extensibility
* Decoupling Services
* Fault Tolerant
* Availability, 
* Disaster Recovery
* Resilient
* Data Consistency
* Single point of failure
* Asynchronous Processing
* Self Healing 
* Security & Privacy
* Cost Effective
* deployment and roll backs in case of failures
* Monitoring
* Logging
* Multi-processing, threading


## API Project Steps
--------------------
1. DB provision
   sharded, db backup, replicas (read, primary write), multi az, IOPs 

2. DB connection code library
   - Connection factory, manage DB threads 
   
3. Model, backbone 
   - service 
  
4. controller (webserver, url handlling)

5. deployment (containers, kubernetes)
   5.1 autoscalling 
   5.2 monitoring 
   5.3 dashboard health
   5.4 Load balancer 
   5.5 multi az
   
6. test cases (unit, functional, stress/performance)
7. Logging (sumologic, splunk, web server logs, stack logs)
8. CICD
   - git (repo) 
      - code reviews, rules implemented
   - circleci/jenkins

9. Static code analysis (sonarqube)

10. APM (performance montiroing )
    - new relic 
    
11. Swaggar documentation



## Optimistic Locking vs. Pesimistic Locking
--------------------------------------------
* OL: operations first, see if no one updated the db and then lock and perform xtion
* PL: Lock the db before operations and then perform the transaction

## Strong vs. Eventual Consistency:
-----------------------------------
* SC: read always see latest write
* EC: read will eventually see latest write

## CAP Theorem (Brewer's theorem):
-----------------------------------
it is impossible for a distributed data store to simultaneously provide more than 
two out of the following three guarantees

* Consistency: Every read receives the most recent write or an error
* Availability: Every request receives a (non-error) response, 
  without the guarantee that it contains the most recent write
* Partition Tolerance: The system continues to operate despite an arbitrary number 
  of messages being dropped (or delayed) by the network between nodes

## Serverless
* Advantages
  + No server management
  + Flexible Scaling
  + Pay for value
  + Automated High Availability and FT


## ELK (Elastic search, Log Stash, Kibana)
------------------------------------------
* 



## Consistent hashing:
----------------------
a consistent hashing function maps its input to evenly distributed outputs, and if the number of shards changes slightly, the output location changes only slightly.

