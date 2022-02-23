## Partitioning / Speeding Techniques:
--------------------------------------
* Indexing
* Sharding: Horizontal Partitioning: Use data id/key to break data into partitions
  + Consistent Hashing

* Vertical Partitionning: Use columns to partition data

## Types:
---------

### Key Value Store: 
--------------------------------
* Zookeeper

### RDBMS: Postgres, MySQL, Oracle, Amazon Redshift
---------------------------------------------------
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


### NoSql : MongoDB, Cassandra, Amazon Dynamo, Distributed Databases
---------------------------------------------------------------------
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

### Cache: Redis, Mem cache 
---------------------------
  + In Memory vs. SSDs cache
  + Advantages: Faster calls, less network calls, less DB load, faster client computations 
  + Drawbacks: inconsistency, threshing, 
  + Mechanisms: Write through, write back.

### TSDB: InFlux, OpenTSDB
--------------------------


## Properties
-------------

### ACID: 
----------
* atomicity, consistency, isolation, durability
* Relational Databases

### BASE 
---------
* Basic Availability Soft-State Eventual Consistency
* No SQL DBs