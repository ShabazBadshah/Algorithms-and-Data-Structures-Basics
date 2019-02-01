# MongoDB

__By__: Shabaz Badshah

__Date__: January 28, 2019

----

## What is MongoDB

MongoDB is a NoSQL Database, also commonly known as a Non-relational (hence NoSQL) database. MongoDB functions based on collections and documents and exposes a Javascript API that we can use to interact with the database.

MongoDB does not support schemas in contrast to its RDBMS alternatives. Data is instead stored in a format very similar to JSON (Javascript Object Notation) where fields can be added dynamically.

## MongoDB vs Relational Database Management Systems

| RDBMS    | MongoDB    |
|:---------|:-----------|
| Database | Database   |
| Table    | Collection |
| Row      | Document   |
| Column   | Field      |

## MongoDB Database Design and Modelling

## MongoDB Basic Queries

- Select All: db.collection_name.find();
- Select Top X: db.collection_name.find().limit(X);
- Insert Single Document: db.collection_name.insert({field1: "value", field2: "value"});
- Insert Multiple Documents: db.collection_name.insertMany([{field1: "value"}, {field2: "value"}]);
- Update Document: db.collection_name.save({"_id": new ObjectId("abc"), field1: "value", field2: "value"});