

## Key terms
------------
- Table
- Item: row/record/document(MongoDB)
- Primary Key: field uniquely identifying items
  - Primary Key
  - Composite Primary key:
    - Partition key
    - Sort Key
- Attributes: other column fields, have types like string, integer, sets, list



## Best habits
--------------
- Always filter on primary keys 
- If using ID's for primary keys, use sortable ids. UUID's are not sortable, so doesn't make a good choice for primary key. 


## One to Many Relationship Strategies
--------------------------------------

| Primary Key               |                    | Attributes         |            |                                            |
|---------------------------|--------------------|--------------------|------------|--------------------------------------------|
| Partition Key: AuthorName | Sort Key: BookName |                    |            |                                            |
| Stephen King              |                    | AuthorBirthdate    | AuthorName | pricing                                    |
|                           | It                 | September 21, 1947 | 1986       | {"creditCard":50, "cash": 45, "paypal":43} |
|                           |                    | AuthorBirthdate    | AuthorName | pricing                                    |
|                           | The Shining        | September 21, 1947 | 1977       | {"creditCard":1, "paypal":3}               |
|                           |                    | AuthorBirthdate    | AuthorName | pricing                                    |
| J.K. Rowling              | Harry Potter       | July 31, 1965      | 1997       | {"creditCard":4, "cash": 5}                |
|                           |                    |                    |            |                                            |


- Denormalization + complex attributes
  - add Complex object like json as data
  - user when:
    - no access pattern on related items directly
    - Limited number of related items
  - eg: pricing attribute

- Denormalization + Duplication:
  - Use when: 
    - duplicated data is immutable
    - duplicated data doesn't change often or is not replicated much
  eg: Author Birthdate attribute

- Composite primary key + query
  - like single table design mentioned below


## Single Table Design
----------------------
- use generic names for primary and sort keys (like pk and sk) 
- eg table:

|    Primary Key    |                    | Attributes        |                   |
|:-----------------:|:------------------:|-------------------|-------------------|
| Partition Key: PK | Sort Key: SK       |                   |                   |
|                   |                    |                   |                   |
| ORG#BERKSHIRE     |                    | OrgName           | SubscriptionLevel |
|                   | ORG#BERKSHIRE      | Berkshire Hathway | Enterprise        |
|                   |                    | UserName          | Role              |
|                   | USER#CHARLIEMUNGER | Charlie Munger    | Member            |
|                   |                    | UserName          | Role              |
|                   | USER#WARRENBUFFETT | Role              | Admin             |
|                   |                    |                   |                   |
| ORG#FACEBOOK      |                    | OrgName           | SubscriptionLevel |
|                   | ORG#FACEBOOK       | Facebook          | Pro               |
|                   |                    | UserName          | Role              |
|                   | USER#SHERYLSANDBERG| Sheryl Sandberg   | Admin             |
|                   |                    |                   |                   |
|                   |                    |                   |                   |