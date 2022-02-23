# AWS Services
---------------
https://aws.amazon.com

## Glossary

* Availability Zone: 
  A data center or a building or an area with multiple buildings

* Region: 
  A Region is a geographically self-contained area where all of the resources you 
  need for your application, all the compute, all the storage, are contained. 
  It's going to be inside a single country boundary bounded by a single set of laws.
  
  + Factors to select a region:
    - Latency
    - Cost
    - Compliance
    - Services availability

  * Includes:
    - At least two availability zones acting as a DR pair, 
      separated by miles of distance and connected by fibre channel network
    
* Tags: 
  Key value pairs, common tags eg: (instance name, department, etc.)

* Security Group:
  eg: web-security-group (allows web access)

* Lightsail:
  predefined tech stacks and deployments (eg. Wordpress, LAMP stack, Node.js, MEAN, etc.)

* Well-Architected Tool: CORPS 
  - Cost Optimization
  - Operational Excellence
  - Reliability
  - Performance Efficiency
  - Security

## Security 
* AWS Organizations
  + create and manage multiple AWS accounts
  + consolidated billing

* IAM (AWS Identity and Access Management)
  + create and manage AWS users in groups and use permissions to allow and 
    deny the access to it appears resource. 
  + RBAC
  + Policy 
    - AWS managed policy: a stain along policy that is created and administrated by AWS. 
      managed policy are designed to provide permission for many common use cases. 
    - customer managed policy: is a stain alone policy that you create and administer in your AWS account. 
    - Inline policy: a policy that's embedded in a principle entity such as a user, a group or a role. 

* AWS Single Sign-On (SSO)
  
* Amazon Cloud Directory
  - you can create a directory for a variety of used cases such as 
    organizational charge, course catalogs, and divine registry. 

* Amazon Cognito

* AWS CloudTrail

* AWS KMS (Key Management Service): 
  create and manage cryptographic keys

* AWS CloudHSM
  cloud-based hardware security module (HSM) that enables you to easily generate 
  and use your own encryption keys on the AWS Cloud.

* AWS API Gateway

* AWS Shield
  - a managed Distributed Denial of Service (DDoS) protection service

* AWS WAF (Web application firewall)
  - helps protect your web applications from common web exploits 
  - like password trials/rate limits/ etc.

* AWS Secret Manager


## Networking
* ELB (Elastic Load Balancer)
  + Types
    - Application Load Balancer
      - Layer 7
    - Network Load Balancer
      - Layer 4
    - Classic Load Balancer 

  + associated to: 1 IP , listening port, 1 VPC, multiple Availability zone, multiple Subnet
  + Target group: group of servers it's going to LB

* VPC (Virtual Private Cloud):
  + VPC is like a virtual box around all your applications. 
  + can contain multiple subnets
  + IP Range: (eg: 10.10.0.0/16), first 16 bits are frozen
    everything inside VPC will be in this IP Range. 
  + By default a multi availability zone structure
  + There are two types of VPC endpoints:
    - Gateway Endpoint
    - Interface Endpoint

* Subnet: 
  + attached to a VPC
  + attached to an Availability zone
  + used to separate out traffic inside a VPC
  + IP Range or IPv4 CIDR Block: (eg: 10.10.1.0/24), first 24 bits are frozen
    everything inside this subnet will be in this IP Range. 
  + Can be public or private

* IGW (Internet Gateway):
  + Create an IGW and attach it to VPC to allow internet traffic to reach inside VPC

* VGW (Virtual Private Gateway):
  + can be associated with your private subnets
  + eg usage: a DBA connecting to a DB in private subnet over companies VPN and 
    doesn't have to go through IGW

* Route Table: 
  + allows what type of traffic anc where it is allowed. 
  + Attached to a VPC, associated to a public subnet (eg: 10.10.1.0/24)
  + eg. entry, traffic from internet to my-igw 
    0.0.0.0/0       my-igw

* NACLs (Network Access Control Lists)

* Security Groups:
  + Act as a firewall for associated Amazon EC2 instances, controlling both inbound and 
    outbound traffic at the instance level



## Compute
----------

* EC2 (Elastic Compute Cloud)
  + AMI (Amazon Machine Image)
    - Contains EC2 instance deployment info

  + Each instance contains a boot volume and a data volume. These are generally EBS volumes.
    - Instance can be turned off and started from where left off. 
    - Helps in saving cost and re-adjusting the compute power

  + Auto Scaling groups

* lambda: 
  run code without provisioning or managing servers. Run functions.

## Storage
----------
* Object storage vs. Block Storage
  + In OS the whole object needs to change during replacing. 
    In Block storage individual blocks of the data can be changed. 

  + OS: S3;
    BS: RDS, EBS

* S3 (Simple Storage Service)
  + durable and scalable store for items like images, videos, text files, and more.
  + stores data in Buckets 
  + Bucket size is not limited
  + Object size ranges from 1 byte to 5 TB
 
* S3 Glacier
  + Data archiving and long term backup

* Amazon CloudFront:
  + Content Delivery Network

* EFS (Elastic File System):
  + for file storage and shared file systems
  + can be accessed over multiple subnets, Availability zones or even VPCs

* EBS (Elastic Block Store):
  - Used for Storage for databases and EC2 instances
  - Amazon EBS can attach to only one EC2 instance at a time.
  - EBS and EC2 instances should be in the same Availability zones

### Comparison
* Cost: 
  S3 is cheapest (price parameters: cost per number of requests made, S3 Analytics, and data transfer out of S3 per gigabyte).
  EFS has the simplest cost structure

* Accessibility:
  S3 can be accessed from anywhere. AWS EBS is only available in a particular region, while you can share files between regions on multiple EFS instances.

* Speed:
  EBS and EFS are both faster than Amazon S3, with high IOPS and lower latency.

* Scalability: 
  EBS is scalable up or down with a single API call. 
  Since EBS is cheaper than EFS, you can use it for database backups and 
  other low-latency interactive applications that require consistent, 
  predictable performance.

* Usage: 
  EFS is best used for large quantities of data, such as large analytic workloads.
  Data at this scale cannot be stored on a single EC2 instance allowed in
  EBS—requiring users to break up data and distribute it between EBS instances. 
  The EFS service allows concurrent access to thousands of EC2 instances, 
  making it possible to process and analyze large amounts of data seamlessly.

## Database
------------
* Relational
  + Aurora:
    MySQL and PostgreSQL-compatible relational database built for the cloud.
    Performance and availability of commercial-grade databases at 1/10th the cost 
  
  + RDS: 
    Set up, operate, and scale a relational database in the cloud with just a few clicks 

  + Redshift: 
    The most popular and fastest cloud data warehouse

* Key-value
  + DynamoDB: 
    Fast and flexible NoSQL database service for any scale

* In-memory
  + ElastiCache for Memcached: 
    Managed, Memcached-compatible, in-memory store. 
    Sub-millisecond latency to power real-time applications

  + ElastiCache for Redis:
    Redis compatible in-memory data store built for the cloud. 
    Power real-time applications with sub-millisecond latency

* Document
  + DocumentDB (with MongoDB compatibility): 
    Fast, scalable, highly available MongoDB-compatible database service

* Wide column
  + Keyspaces (for Apache Cassandra): 
    Managed Cassandra-compatible database

* Graph
  + Neptune:
    Fast, reliable graph database built for the cloud

* Time series
  + Timestream:
    Fast, scalable, fully managed time series database

## Management
-------------
* CloudFormation:
  provides a common language to describe and provision all the infrastructure resources in your environment
  (https://aws.amazon.com/cloudformation/)

  + Stacks: a collection of AWS resources that you can manage as a single unit. 
    More like a Logical Aggregation of resources.
  + StackSets: enables you to create, update, or delete stacks across multiple accounts 
    and regions with a single operation
  + Change sets: allow you to preview how proposed changes to a stack might impact your 
    running resources, making changes to your stack only when you decide
  + Drift detection: Run drift detection to identify configuration changes between your 
    live resources and the template. Drifts will be detected on stacks and resources

* Cloudwatch:
  monitoring and observability service

* TSO Logic:
  provides discovery of your existing resources to help identify what you are 
  running in your compute, storage, data base, and other areas.
  TCO (Total cost of ownership)

## Analytics
------------
* ElasticSearch Service

* Athena: 
  interactive query service that makes it easy to analyze data in Amazon S3 
  using standard SQL.

* Kinesis: 
  collect, process and analyze data streams in real time.

* Glue
  + AWS Glue is a fully managed ETL (Extract, transform and load)
  + Used to categorize, clean, enrich and move data reliably between various data stores

  + Terminologies:
    - Data Catalog:
      Persistent Metadata store, contains table definitions, job definitions, and other control info. Each AWS account has one data catalog per region

    - Classifier: Determines the schema of data (csv, json, yaml, properties, rdbms, or custom)

    - Connection: 
      properties to connect to Data store

    - Crawlers:
      program that connects to a data store

    - Database:
      Set of associated Data catalog table definitions organized into a logical group

    - Data Store: S3, RDBMS
    - Data source
    - data target

    - Development endpoint:
      Environment to develop and test ETL scripts

    - Job: 
      business logic to perform ETL work.
      contains transformation script, data sources, data targets

    - Notebook server
      webbased environment to run pyspark statements

    - Script: pyspark or scala
    - Table
    - Transform
    - Trigger

## Containers
-------------
* ECS (Elastic Container Service)
  deploy, manage, and scale Docker containers running applications, services, and batch processes.

* ECR (Elastic Container Registry)
  a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images

* EKS (Elastic Kubernetes Service)

* Task Definition: 
  + a blueprint of task/application
  + json file that describes one or more containers, launch types (EC2, Fargate), ports, network
  + Given to an orchestration Service (ECS or EKS)

* Hierarchy:
  + Cluster
    - Service
      - Task Definition
        - Container Definition


## Queues
---------
* SQS (Simple Queue Service)
  + message retention period : default 4 days, range 60 secs - 14 days
  + Types:
    - Default Q, or Standard Q

      - Unlimited Transactions per sec per action
      - at-least-once message delivery
      - delivery might be out of order

    - FIFO Q
      - First in first out, critical events, no duplicates
      - upto 3k messages per sec with batching
      - 300 messages per sec per action

## Tools
---------
* Troposphere: 
  
  troposphere library allows for easier creation of the AWS CloudFormation JSON
  by writing Python code to describe the AWS resources.
  (https://github.com/cloudtools/troposphere)

* CLI:

  The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services.
  (https://aws.amazon.com/cli/)

* aws-es-proxy
  a small web server application sitting between your HTTP client (browser, curl, etc...) and 
  Amazon Elasticsearch service. It will sign your requests using latest AWS Signature Version 4 
  before sending the request to Amazon Elasticsearch. When response is back from Amazon Elasticsearch, 
  this response will be sent back to your HTTP client.
  https://github.com/abutaha/aws-es-proxy

  install using 'brew install aws-es-proxy'

* django-eb-sqs
  an open source simple task manager for AWS SQS. It uses SQS and the boto3 library. 
  (https://github.com/cuda-networks/django-eb-sqs)


## Migration

* Phases 
  1. Migration Preparation and business planning
  2. Portfolio discovery and planning
  3. Designing
  4. Migrating and Validating your applications
  5. Operate

* six approaches that are common migration strategies for applications
  1. Rehost
  2. Replatform
  3. Repurchase
  4. Refactor or re-architect
  5. Retire
  6. Retain

* AWS Migration service. 
* Cloud Endure
* AWS DMS (Database Migration Service)
* AWS SMS (Server Migration Service)

## Chat Bots
* Amazon Lex : conversational interfaces into any application using voice and text. 
  + Bot Concepts
    - Intent
    - Slot
    - Lambda
    - Confirmation
    - Fulfillment

* Amazon Polly: turns text into lifelike speech, allowing you to create applications that talk
