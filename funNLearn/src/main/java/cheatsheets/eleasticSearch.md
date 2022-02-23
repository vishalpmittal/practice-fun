* REST based Querying
* Written in Java, build on Apache Lucene
* Easy to get started
* Highly scalable, distributed by nature
* Designed to take data from any source, analyze it and search through it


## Basic Terms
--------------
* Hierarchy
  + indices 
    - types
      - Documents
        - Fields

* Indices:
  + An index powers search into all documents within a collection of types. 
  + they contain inverted indices that let you search across everything within them at once. 
  + RDBMS: more like a database

* Types:
  + A type defines the schema and mapping shared by documents that represent the same sort of thing. eg. a log entry, an encyclopedia article, etc. 
  + RDBMS: lot like a table

* Documents: 
  + Documents are the things you are searching for. 
  + They can be more than text - any structured JSON data works. 
  + Every document has a unique ID, and a type. 
  + RDBMS: A lot like a row
  + It's a Json Object containing many fields

* Fields
  + these are more like columns in an RDBMS

## Inverted Indexing
--------------------
Document 1:
Space: the final frontier. these are the voyages

Document 2:
He's bad, he's number one. He's the space cowboy with the laser gun!

```
Inverted index:
space: 1, 2
the: 1, 2
final: 1
frontier: 1
he: 2
bad: 2
```

## TF-IDF: (Term Frequency * Inverse Document Frequency)
--------------------------------------------------------
* Relevance:
  + The word 'the' is a very common word
  + return 'the' where it is really relevant or is of high importance.

* Term Frequency is how often a term appears in a given document. 
  * the: 2, space: 1
* Document Frequency is how often a term appears in all documents
  * the: 4, space: 2

* Term Frequency/Document Frequency measures the relevance of a term in a document.

## Scaling
----------
* Distributed Sharding: 
  + An index is split into shards
  + Documents are hashed to a particular shard
  + Each shard may be on a different node in a cluster
  + every shard is a self-contained Lucene index of its own.

* Fault tolerance 
  - Let's say we have two shared, then primary and replica's of 2 shards is distributed amongst 3 Node's:
  ```
    Node1 : P1, R0 
    Node2 : R1, R0 
    Node3 : P0, R1 
  ```

  - Odd number of nodes is always a good idea
  - Round robin scheme works in the cluster
  - Write: requests are routed to the primary shard, then replicated
  - Read: requests are routed to the primary or any replica

```NOTE
- The number of primary shards cannot be changed later. 
- You can add more replica shards for more read throughput though. 
- Worst case you can re-index your data.
- the number of shards can be setup front via a PUT REST 

PUT /testindex : 3 primary and 1 replicas so total of 6 shards
{
    "settings": {
        "number_of_shards": 3,
        "number_of_replicas": 1
    }
}
```

## ElasticSearch Query DSL (Domain Specific Language) 
-----------------------------------------------------
* https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html

*  wildcard: returns all hits, 
   + GET /ecommerce/product/_search?q=*       
```python
"hits": {
    "total": 1000,
    "max_score": 1,
    "hits" : [
        {
            "_index" : "ecommerce",
            "_type": "product",
            "_id": "14"
            "_score": 1,
            "_source": {
                "name": "...",
                ....
                ....
            }
        }
    ]
}
```

* String Search
  + GET /ecommerce/product/_search?q=pasta      , or
  + GET /ecommerce/product/_search?q=name:pasta
  + GET /ecommerce/product/_search?q=description:pasta 
```python
"hits": {
    "total": 10,
    "max_score": 0.82480276,
    "hits" : [
        {
            "_index" : "ecommerce",
            "_type": "product",
            "_id": "166"
            "_score": 0.82480276,
            "_source": {
                "name": "Pasta - Angel Hair",
                "description": "....",
                ....
            }
        }
    ]
}

```
* Examples

  + title field contains "search" and content field contains "elasticsearch" and status field contains "published" and publish_date field contains a date from 1 Jan 2015 onwards.
    ```bash
    curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'
    {
      "query": { 
        "bool": { 
          "must": [
            { "match": { "title":   "Search"        }},
            { "match": { "content": "Elasticsearch" }}
          ],
          "filter": [ 
            { "term":  { "status": "published" }},
            { "range": { "publish_date": { "gte": "2015-01-01" }}}
          ]
        }
      }
    }
    '
    ```

* Compound queries
  + https://www.elastic.co/guide/en/elasticsearch/reference/current/compound-queries.html#compound-queries

  + bool: must, filter, should, must_not
    - matches documents matching boolean combinations of other queries. 

  + boosting: positive, negative, negative_boost
    - documents matching a positive query while reducing the relevance score of documents that also match a negative query.

  + constant_score: filter, boost
    - Wraps a filter query and returns every matching document with a relevance score equal to the boost parameter value.

  + dis_max (Disjunction Max): queries, tie_breaker
    - Returns documents matching one or more wrapped queries, called query clauses or clauses

  + function_score
    - allows you to modify the score of documents that are retrieved by a query.
- 


## Kibana
---------
* Explore and visualize your elastic search data.

* Sense
  + Kibana plugin to visualize data


## keep Elasticsearch synchronized with a RDBMS using Logstash and JDBC

* https://www.elastic.co/blog/how-to-keep-elasticsearch-synchronized-with-a-relational-database-using-logstash

