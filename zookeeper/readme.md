Zookeeper
=============================
Zookeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.

-  Highly available
-  Manages shared state of any kind
-  Transaction control (Atomic operations)
-  Lock management

Architecture
------------------
-  it's a metadata server
-  Written in java
-  official API's in C and Java
-  In-memory database (on-heap)
-  ensemble
    -  Minimum of three nodes for a quorum
-  all nodes participate in read/write

Data Model
------------------
-  it is just like a Linux file structure. 
-  every directory is called a znode
-  it is hierarchical like linux
-  /
   |- znode1
   |  |- znode11
   |  |- znode12   
   |
   |- znode2
    ......

-  znode is a byte array (~10 K Max)
-  Timestamped
-  independent, non-inherited ACLs
-  Versioned
-  zero or more child ZNodes
-  Persistent or session-ephemeral
-  Counting ZNodes

Sessions
-----------------
-  Connection between the client and a node in the ensemble
-  Ephemeral nodes live and die with sessions

Watches
----------------
-  One-time triggers on ZNodes values or children
-  Asynchronous
-  Guaranteed to be seen by the client before the data change is seen by the client

ACLs
-----------------
-  Apply to individual ZNodes (no inheritance, not children)

-  ZNode contains a list of IDs
    -  world (everyone)
    -  auth (anyone who signed in)
    -  digest (hash of the username and password who signed in)
    -  ip (any client connected from a particular ip)

-  IDs have permissions
    -  CREATE, READ, WRITE, DELETE, ADMIN  

Use Case: Leader Election
----------------------------------
-  Create a ZNode called leader-election
-  all candidates create ephemeral sequential children
-  the child of leader-election with the smalled sequence number is leader
-  Watch the ZNode with the next smallest sequence number for good news. (so i get to be the next leader)

Use Case: Distributed Locks
----------------------------------
-  Setup: create a ZNode called resource
-  create ephemeral node called
    resource/hostname-{i}
-  Examine children of resource; I hold the lock if my ID is lowest
-  Otherwise watch the ID preceding mine
-  Upon update event, I hold the lock
-  To release the lock, delete the ephemeral node





