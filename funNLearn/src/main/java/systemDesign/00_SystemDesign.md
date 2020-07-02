Features
Define APIs
Availability
Scalability
Durability
Class Diagram
Security & Privacy
Cost Effective


* Optimistic Locking vs. Pesimistic Locking
  + OL: operations first, see if no one updated the db and then lock and perform xtion
  + PL: Lock the db before operations and then perform the transaction

* Strong vs. Eventual Consistency:
  + SC: read always see latest write
  + EC: read will eventually see latest write



### CAP Theorem (Brewer's theorem):

-----------------------------------
it is impossible for a distributed data store to simultaneously provide more than 
two out of the following three guarantees

*  Consistency: Every read receives the most recent write or an error
*  Availability: Every request receives a (non-error) response, 

                 without the guarantee that it contains the most recent write

*  Partition Tolerance: The system continues to operate despite an arbitrary number 

                 of messages being dropped (or delayed) by the network between nodes

## Database: 
------------

### Partitioning / Speeding Techniques:
* Indexing
* Sharding: Horizontal Partitioning: Use data id/key to break data into partitions
  + Consistent Hashing

* Vertical Partitionning: Use columns to partition data

### Types:
* Key Value Store : Zookeeper
--------------------------------



* RDBMS: Postgres, MySQL, Oracle
--------------------------------
  + Pluses
    - Insertions and retrievals can be done with parts of data, you do 
      not need the whole block of data
    - Read operations are more easier
    - Financial transactions use RDBMS
  + Minuses
    - predefined schema, any schema update locks the whole table and is very
      expensive
    - Joins are very expensive to join blocks of data from different tables
    - if we do not know the number of relationships like how many addresses a
      a person can have then we have to create a mapping table. another example 
      is threaded emails.

* NoSql : MongoDB, Cassandra, Amazon Dynamo, Distributed Databases
-------------------------------------------------------------------
  + Usage:
    a blocked data, with more writes, less read and updates, 

  + Minuses:
    - Insertions and retrievals need the whole block of data.
    - Updates = Deletion + insertion. which is more expensive. 
    - ACID is not guaranteed and hence transactions are not possible here 
    - Read operations are comparitively slower
    - relations are not implicit and joins are pretty much manual

  + Pluses: 
    - build for scalibility. horizontal partitioning is easier since the block of 
      data stays together. 

    - Flexible schema: 
      no strict schema, like a person can or can not have a middle name
      if we do not know the number of relationships like how many child emails 
      are in a parent email, that would be no problem here. 

    - All relavent data is together in one block so Joins are not needed. 
    - Build for metrics/analysis/aggregations

* Cache: Redis, Mem cache, 
  + In Memory vs. SSDs cache
  + Advantages: Faster calls, less network calls, less DB load, faster client computations 
  + Drawbacks: inconsistency, threshing, 
  + Mechanisms: Write through, write back.

* TSDB: InFlux, OpenTSDB

* ACID: atomicity, consistency, isolation, durability
Relational Databases

* BASE : Basic Availability Soft-State Eventual Consistency
No SQL DBs

## Characterstics of a good design:

* Scalability
  + Horizontal scaling : distributed system
  + Vertical scaling : add more CPU RAM storage etc...

* Extensibility
* Decoupling Services
* Fault Tolerant
* Desaster Recovery
* Resilient
* Data Consistency
* Single point of failure
* Asynchronous Processsing
* Logging
* Self Healing 

## Architectures:

* Monolithic Architecture
* Microservices Architecture
* Distributed Systems

## Components

* Load Balancer
  + Technique 1 : client ID key hashing
  + Technique 2 : LRU

* Web Sockets
* HTTP
  + Long polling 

## Techniques


## Monotoring / Metrics

* SLI, SLO, KTLO, KPI, Uptime
* Incident
* Service Discovery
* Heartbeat Maintainance

* Service Level Indicator (SLI): a carefully defined quantitative measure of

  some aspect of the level of service that is provided.eg: the
  success rate of requests to a particular REST endpoint is the SLI.

* Service Level Objective (SLO): a target value or range of values for a

  service level that is measured by an SLI.eg: the minumum
  success rate of requests to a particular endpoint of a service is the SLO
  for that endpoint.

* Incident: an event that begins when the `SLI<SLO` and ends when `SLI>=SLO` 

* ATTR - Average Time To Repair
* MTTR - Mean Time To Repair




## Security

### Key Terms

* UBAC : User Based Access Control
* ACL: Access Control List
* Authorization: Allowed?
* Authentication: logging In?
* Technologies: LDAP, Active Directory, Open LDAP

* Gateway service
* Profile Service 

* SSL

DFS (Distributed File System)
NFS 

Retrial
Ordering 
Imdempotency
Depriotizing 

## API Design:

* Always version your api /v1/... 
* No verbs in the api url, use already provided GET, POST, PUT, DELETE
* For huge result sets use:
  + Pagination
  + Fragmentation
