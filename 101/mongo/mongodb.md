# MongoDB

__By__: Shabaz Badshah

__Date__: January 28, 2019

----

## What is MongoDB

MongoDB is a NoSQL Database, also commonly known as a Non-relational (hence NoSQL) database. MongoDB functions based on collections and documents and exposes a Javascript API that we can use to interact with the database.

MongoDB does not support schemas in contrast to its RDBMS alternatives. Data is instead stored in a format very similar to JSON (Javascript Object Notation) where fields can be added dynamically.

## MongoDB vs Relational Database Management Systems

| RDBMS (Relational Database Management Systems) | MongoDB         |
|:-----------------------------------------------|:----------------|
| Database                                       | Database        |
| Table                                          | Collection      |
| Row                                            | Document        |
| Field                                          | Key:Value Pairs |

- MongoDB does not support foreign key constraints
- MongoDB does not support *Joins*, these are done at the application level
- There may be inconsistencies of data since data can be repeated between multiple collections
- MongoDB schemas are dynamic, fields can be added at any time
- Normalization/De-normalization is not required, set up the schema based on application requirements

### Example Data in PostgreSQL vs MongoDB

#### PostgreSQL Data Representation

![An example table of student's, their courses, and their grades](./student-data-model-postgresql.png "An example table of student's, their courses, and their grades")

#### MongoDB Data Representation

A Student collection which contains two documents of students and their course information

```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "studentId": 100,
  "firstName": "Jonathan",
  "middleName": "Eli",
  "lastName": "Tobin",
  "classes": [
    {
      "courseId": "PHY101",
      "grade": "B",
      "courseName": "Physics 101",
      "credits": 3
    },
    {
      "courseId": "BUS101",
      "grade": "B+",
      "courseName": "Business 101",
      "credits": 3
    }
  ]
},
{
  "_id": ObjectId("507f191e810c19729de860ea"),
  "studentId": 101,
  "firstName": "Meathead",
  "middleName": "Rob",
  "lastName": "Lowe",
  "classes": [
    {
      "courseId": "PHY101",
      "grade": "F",
      "courseName": "Physics 101",
      "credits": 3
    }
  ]
},
```

## MongoDB Database Design and Modelling

MongoDB schemas can be designed in two ways. Since Mongo does not utilize tables to organize data, and does not support joins, we utilize *embedding* and *referencing* to associate documents with other collections.

### Embedding

Embedding is the process where common data that is referenced often is moved into the parent document to reduce additional queries.

In the example above, we could have made the *"classes"* field into its own *classes* collection and queried for both students and all of their classes. Instead of requiring an additional query, we structured our student object to contain the classes associated to the student.

__Embedding Data:__

- Embed data when it will be queried very often
- Embed data when the fields that are commonly queried are fairly *static* and don't change often
- Embed data when there is a one-to-one relationship between two pieces of data
- Can possibly embed data if there exists a one-to-many relationship (referencing can also be used as well)
- Embedding data reduces the amount of queries required for the database

__Operations on Embedded Data:__:

- Performing insert and update operations on a single document is *atomic*
- Insert operations are fairly quick
- Querying operations are very quick
- Updating operations can be very complex since the data may need to be updated in multiple locations
  - Data will "eventually" be consistent

### Referencing

Referencing is similar to its RDBMS counterparts where common data can be stored in one location and be linked from multiple different locations.

If we take the student classes example from above and refactor the data model to use reference instead,here is what we would get. Pay attention to the "classes" ObjectId and the "_id" of the class that has been referenced.

```json
Student Document

{
  "_id": ObjectId("507f191e810c19729de860ea"),
  "studentId": 101,
  "firstName": "Meathead",
  "middleName": "Rob",
  "lastName": "Lowe",
  "classes": [
    ObjectId("54759eb3c090d83494e2d804")
  ]
}


Classes Document

{
  "_id": ObjectId("54759eb3c090d83494e2d804"),
  "studentId": ObjectId("507f191e810c19729de860ea"),
  "courseId": "PHY101",
  "grade": "F",
  "courseName": "Physics 101",
  "credits": 3
}
```

__Referencing Data:__

- Reference data when there is a one-to-many relationship
- Reference data when it's important for it to be consistent (i.e. we keep the important data in one place)
- Reference data that is not often required to be queried; data that is not accessed often
- If the document size may increase past 16MB, then referencing *must* be used

__Operations on Referenced Data:__:

- Insert operations are very quick
- Querying operations may be more inefficient then embedding since multiple queries would be required to retrieve data
- Updating operations would be very quick since you only need to update the data in one location

### Denormalizing

- TODO

### Embedding vs Referencing

| Embedding                                         | Referencing                                                              |
|:--------------------------------------------------|:-------------------------------------------------------------------------|
| Better for data that will be accessed often       | Better for data that will not be accessed often                          |
| Use for data that does not change frequently      | Use for data that is required to be consistent across multiple documents and may be used in many places |
| Querying and inserting data is efficient          | Updating and inserting data is very efficient                            |
| Write operations are atomic at the document level |                                                                          |

## Common Design Guidelines

- Don't force relationships on data, MongoDB is not created for relationships between data
- Try to store data in a single document if possible (i.e. embedding)
- Design you schema based around how the data will be queried. Structure your data model to be the most performant

## MongoDB Basic Queries

__Creating Collections:__

- __Create collection:__ db.createCollection("collection_name");
- __Create new collection with data:__ db.collection_name.insertOne({}, {"key1": "a", "key2": "b"} );

__Dropping Collections:__

- __Drop collection:__ db.dropCollection("collection_name");

__Querying Data:__

- __Select all:__ db.collection_name.find();g
- __Select specific keys:__ db.collection_name.find({}, {"_id": 0, key1": 1, "key5": 1});
- __Select all with specific condition:__ db.collection_name.find({"key1": "value"});
- __Select specific keys with specific conditions:__ db.collection_name.find({"key1": "value1"}, {"_id": 0, key1": 1, "key5": 1})

__Inserting Data:__

- __Insert single document:__ db.collection_name.insertOne({field1: "value", field2: "value"});
- __Insert multiple documents:__ db.collection_name.insertMany([ {field1: "value"}, {field2: "value"} ]);

__Updating Data:__

- __Update document:__ db.collection_name.save({"_id": new ObjectId("abc"), field1: "value", field2: "value"});
- __Add key to existing collection:__ db.collection_name.updateMany({}, {$set: {"key1": "a"}});
- __Remove key from existing collection:__ db.collection_name.updateMany({}, {$unset: {"key1": ""}});

__Deleting Data:__

- __Delete data with specific key:__ db.collection_name.deleteOne({"key1": "value1"});
- __Delete all data with specific key:__ db.collection_name.deleteMany({"key1": "value1"});
- __Delete everything from collection:__ db.collection_name.deleteMany({});

__Other:__

- __Count:__ db.collection_name.count();
- __Sort with key in ascending order:__ db.collection_name.find().sort({"key": 1});
- __Distinct elements:__ db.collection_name.find().distinct();
- __Grab first X results:__ db.collection_name.find().limit(X);

## Further Reading

- https://www.slideshare.net/interviewcoach/mongodb-best-practices
- https://dev.to/mrm8488/mongodb-schema-design-patterns-i-4gdp
