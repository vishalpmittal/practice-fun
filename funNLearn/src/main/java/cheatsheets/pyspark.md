



### Create a dataframe from list of data
```python
    from pyspark.context import SparkContext
    from pyspark.sql import SQLContext

    sc = SparkContext.getOrCreate()
    sqlc = SQLContext(sc)

    df1 = sqlc.createDataFrame([
        (1, 'vc11', 'vc21', True),
        (2, 'vc12', 'vc22', False),
        (3, 'vc13', 'vc23', True)
    ], ["id", 'c1', 'c2', 'c3'])

    df2 = sqlc.createDataFrame([
        (1, 'vc11', 'vc21', None),
        (2, 'vc12', 'vc22', False),
        (3, 'vc13', 'vc23', True)
    ], ["id", 'c1', 'c2', 'c3'])
```

### Create a dataframe from Json
```python
    newJson = {
        "time":"2020-10-05T04:30:00.552223",
        "duration":86400,
        "source_type":"v1",
        "event_feed":"m1",
        "metric":"counts",
        "resource":"email",
        "source":"test_source",
        "source_details":{"account_id":"xydid","bcc_id":"124"},
        "usage":1234,
        "uuid":"c1234c23-e8f0-4b67-bb56-14c714987977"
    }
    df = sqlc.read.json(sc.parallelize([newJson]))
```

### Loop through each row of Dataframe 
--------------------------------------
```python
# Create the dataframe
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = [
    ('James','Smith','M',30),('Anna','Rose','F',41),
    ('Robert','Williams','M',62),
]
columns = ["firstname", "lastname", "gender", "salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()

# Refering columns by index.
rdd=df.rdd.map(lambda x: (x[0] + "," + x[1], x[2], x[3]*2))  
df2=rdd.toDF(["name", "gender", "new_salary"])
df2.show()

# Referring Column Names
rdd2=df.rdd.map(lambda x: (x["firstname"]+","+x["lastname"],x["gender"],x["salary"]*2)) 

# Referring Column Names
rdd2=df.rdd.map(lambda x: (x.firstname + "," + x.lastname, x.gender, x.salary*2))

```

### Create a json from dataframe
--------------------------------
```python
import json
list_of_json_strings=df.toJSON().collect()
list_of_jsons = [json.loads(x) for x in list_of_json_strings]
```


### Misc:
```python
    # replace null values with False
    df2.fillna({'c3':False}).show()

    
```


