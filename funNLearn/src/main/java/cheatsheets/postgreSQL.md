## DB OS level Commands
---------------------
```bash
psql people vishal    # connect as vishal to people database

dropdb --host=localhost --username=postgres --port=5432 users --password=postgres
createuser --host=localhost --username=postgres --port=5432 --createdb --pwprompt vishal
createdb  --host=localhost --username=postgres --port=5432 --owner=vishal users

pg_restore -x --verbose --host=localhost --username=vishal --port=5432 --dbname=users users_backup.dmp >restore_logs.txt 2>&1
```

## Backslash pgsql commands
---------------------------
```bash
\q                # quit
\dt               # describe/list all table 
\d+ users         # show the schema of users table
\l                # show all databases on the server
\i myfile.sql     # run the sql file on command prompt
\d table_name     # show table schema
\d+ table_name

# Copy data from CSV file to postgres table.
CREATE TABLE track_raw(title TEXT, artist TEXT, album TEXT, count INTEGER, rating INTEGER, len INTEGER);

\copy track_raw(title,artist,album,count,rating,len) FROM 'library.csv' WITH DELIMITER ',' CSV;
```
## Create
---------------------------

```bash
CREATE USER vishal WITH PASSWORD 'secret';
CREATE DATABASE people WITH OWNER 'vishal' ENCODING 'UTF8';

CREATE TABLE users(id SERIAL, name VARCHAR(128), email VARCHAR(128));
CREATE TABLE result (
  id SERIAL, 
  link_id INTEGER UNIQUE,                      # UNIQUE is a logical key, also DB creates an index for it
  score FLOAT,
  percentile DOUBLE NOT NULL,                  # percentile in double and is mandatory
  title VARCHAR(4096), 
  note VARCHAR(4096), 
  debug_log VARCHAR(8192),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  updated_at TIMESTAMP, 
  user_id INTEGER REFERENCE users(id) ON DELETE CASCADE,    # foreign key, on deleting user this record is deleted
  UNIQUE(title, user_id),                          # compound unique key, includes referenced column
  UNIQUE(title, score),                            # Composite primary key
  PRIMARY KEY(id)                             # PRIMARY KEY is an index
);


INSERT INTO users(name, email) VALUES ('vishal', 'abc@xyz.com');

INSERT                                  # album_id and genre_id are foreign keys
INTO track (title, rating, len, count, album_id, genre_id) 
VALUES ('stairway', 5, 482, 0, 2, 1)



```

* Data Types
    + CHAR(n)              # faster for smaller strings < 64 bits. n is length of string
    + VARCHAR(n)           # n is number of characters in string
    + TEXT()               # eg: blog, webpage text
    + SMALLINT()           # (-32768, +32768)
    + INTEGER()            # (2 Billion)
    + BIGINT()             # (~10**18 ish)
    + REAL()               # floating point 32 bit, 10**38 with 7 digits of accuracy
    + DOUBLE PRECISION()   # floating point 64 bit, 10**308 with 14 digits of accuracy
    + NUMERIC(accuracy, decimal)     # 
    + TIMESTAMP()          # YYYY-MM-DD HH:MM:SS
    + DATE()               # YYYY-MM-DD
    + TIME()               # HH:MM:SS
    + NOW()                # postgres built-in function
    + SERIAL()             # auto incremented id field, synchronized over multiple connections

## Read
---------------------------
```bash
SELECT * FROM users WHERE email='abc@xyz.com';

# get 10 records starting 3rd record, sorted by email where name has e
SELECT * FROM users WHERE name LIKE '%e%' ORDER BY email DESC OFFSET 2 LIMIT 10;

# select matching substring ignoring case
SELECT * FROM users WHERE LOWER(name) like LOWER('vishal')
```

## Update
---------------------------
```bash
UPDATE users SET name='abc' WHERE email='abc@xyz.com'; 

ALTER DATABASE "old_db_name" RENAME TO "new_db_name";
```

## Delete
---------------------------
```bash
DELETE FROM users WHERE email='abc@xyz.com';
```

## Glossary
-----------
* Database- contains one or more tables 
* Relation (or table) - contains tuples and attributes 
* Tuple (or row) - a set of fields which generally resent an "object" like a person or a music track. 
* Attribute (also column or field) - of of possibly many elements of data corresponding to the object represented by the row.



* Primary Key
* Logical Key: the key outside world use to identify the record, like email. 
* Foreign Key: reference to primary key of another relation

Database Normalization (3NF)
- do not replicate data
- use integer of keys
- add special key column to each table, which you will make reference to

