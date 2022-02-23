## Kafka 
------------------
- open source distributed pub sub messaging solution 
- stores data in partitions, Partitions store topics, topics are key, value pairs 
- ordering is always preserved 
- default message size 1 MB size 
- default retention is 7 days (can configure)

- consumer has to take care of the retry of message retrieval 
- does not allow consumer to filter messages within a topic before pulling. Consumer has to receive all the messages in a partition . 
- No delayed or scheduled routing. Messages are immediately available to consumer as soon as they arrive. 
- Scales better horizontally 
- Multiple consumers with different type of logic can receive a message 
- can serve both synchronous and asynchronous replication
- kafka connect: get data in and out of kafka
- kafka stream: stream processing of the data
- Yammer Metrics: metrics reporting in the server 

## kinesis
--------------------
- modelled after apache Kafka
- stores data in shards, shards store data records, data records consists of a sequence number, partition key and an immutable data blob (up to 1 MB)
- messages ordered within a shard 
- Max message size 1 MB 
- Data records limit : 5 times per second and up to 2 MB per shard 
- default retention is 24 hours (can configure to max 7 days)
- pay as go model 
- writes synchronously to maintain 3 replications 
- Video Streams, Data streams, Data firehose, Data analytics 
- AWS Cloudwatch : monitoring 

## RabbitMQ
------------------
- Message broker 
- supports both queue, as well as pub sub (topics)
- Minimal guarantee regarding the ordering of messages within a stream 
- out of box support for retry logic 
- ordering is guaranteed only in case of one consumer 
- the topic exchange and header exchange facilitate the consumers with a choice of receiving specific messages 
- messages have limited validity of time to be consumed otherwise removed from the queue 
- provides delayed or scheduled routing. 
- scales better vertically 

## AWS SQS
------------------
- queue based messaging system 
- one or more consumers will read messages
- message is delivered one and only once to a single consumer 
- once a message is processed it gets removed from the queue
- generally all consumers  perform the same type of logic 
- Message order is only preserved in FIFO queue
- Delay queue postpones messages, makes messages invisible, and delays the messages for the duration of 0 to 15 minutes.
- Creating unlimited queues and messages.
- 256 KB default message size 
- Data retention 60 secs - 14 days 

