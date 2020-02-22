# Elasticsearch

## What is Elasticsearch

Elasticsearch is an open source search engine based that provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.

For a layman, 

Elasticsearch as name suggest is ```elastic-search``` i.e., ```scaleable-search```.

This part of the repo is divided in 2 parts and will cover some advance topics in addition to the basics of elasticsearch.

    1. CRUD Operations & perform search queries against documents.
    2. Describe in detail how elasticsearch analyzes and stores the data.

### Highlights

- Built using Apache Lucene
- RESTful (Simple Rest API)
- Elastic refers to high scalability
- High Availability
- Near real-time distributed search and analytics engine
- Good Documentation
- Every field is indexed
- Distributed document store
- Analytics API
- Near real-time distributed indexing
- Native Full-Text search/Google Like search
- Huge community
- Sharding and Replication

## Use Case

- Application Search
- Business Analysis
- Enterprise Search
- Metric Analysis
- Operational Log Analytics
- **and much more...**

## Terminologies

1. Cluster
    - Collection of one or more nodes (servers).
    - A cluster can consist of as many nodes as you want, making it extremely scalable.
    - The collection of nodes contain all of the data in the cluster, and the cluster provides indexing and search capability across all of the nodes.
    - So, no need to worry about which particular node a given document (some data) is stored on.
    - Clusters are identified by a unique name, which defaults to ```elasticsearch```.
    - Each cluster has a single master node which is chosen automatically by the cluster and which can be replaced if the current master node fails.

2. Node
    - A single server that stores searchable data, and is part of a cluster.
    - If a cluster only contains one node, then this node would store all of the data, otherwise this node would contain a subset of a cluster's data.
    - A node is also identified by its name.
    - By default, a node will join a cluster named ```elasticsearch``` unless configured otherwise.
    - Starting a single node on a network, will create a single-node cluster named ```elasticsearch``` by default,

3. Master Node
    - Handles write requests for the cluster and publishes changes to other nodes in an ordered fashion.

4. Index
    - An index is a **collection of documents**.
    - Think of it like a database within a relational database system (not always true though).
    - Indexes are identified by names that you choose, and these names must be lowercased. The names are used when indexing, searching, updating and deleting documents within indexes.
    - You can define as many indexes as you want within a cluster depending on the scale of your project.

5. Type
    - A type represents a class or category of similar documents.
    - Think of it like a table within a relational database system.
    - An index can have one or more types.
    - When searching for a specific type of document, Elasticsearch applies a filter on this ```_type``` field.

6. Mappings
    - A document type has a mapping.
    - Similar to schema of a table in a relational database.
    - It describes the fields that a document of a given type may have along with their data types, such as string, integer, date, etc.
    - It is optional to define a mapping before adding documents to an index.
    - If no mapping is defined, it will be inferred automatically when a document is added, based on its data.

7. Document
    - A document is a basic unit of information that can be indexed.
    - It consists of fields.
    - Documents are expressed as JSON objects.
    - You can store as many documents within an index as you want.
    - A document can be thought of as being the equivalent of a row in a database table.

8. Fields
    - They are key/value pairs, where a value can be of various types, such as strings, dates, objects, etc.
    - The fields of a document correspond to columns for a table.

9. Shards
    - An index can be divided into multiple pieces, and each piece is called a shard.
    - This is useful if an index contains more data than the hardware of a node can store.
    - A shard can then be created and stored on another node which has enough space for it.
    - A shard is a fully functional and independent index and can be stored on any node within a cluster.
    - The number of shards can be specified when creating an index, but it defaults to five.
    - Sharding allows to distribute and parallelize operations across shards, which increases the performance of a cluster.

10. Replica
    - A replica is a copy of a shard, which can take over in case a shard or a node fails.
    - A replica never resides on the same node as the original shard, meaning that if the given node fails, the replica will be available on another node.
    - Replicas also allow for scaling search volume, because replicas can handle search queries.
    - Elasticsearch adds five primary shards and one replica for each index, meaning that unless configured otherwise, there will be one replica for each primary shard, which is five in total.

11. Analysis
    - Analysis is the process of converting full text to terms.
    - A term is an exact value that is indexed in Elasticsearch.
    - Depending on which analyzer is used, these phrases: ```FOO BAR```, ```Foo-Bar```, ```foo,bar``` will probably all result in the terms ```foo``` and ```bar```.
    - A full text query for ```FoO:bAR``` will also be analyzed to the terms ```foo```,```bar``` and will thus match the terms stored in the index.

**Some people confuse Elasticsearch with NoSQL Database but they are not same. ES do provides some of the Features of NoSQL but it primarily is a search and analysis Engine.**