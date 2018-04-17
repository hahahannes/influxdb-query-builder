# influxdb_query_builder
Python query builder for InfluxDB, similar to JDBC for Java. Supports client side prepared statements

# Goal
Because of several reasons, a query builder is needed:
- InfluxDB only supports parameter binding via the HTTP API and only for field and tag values
- [The Python client](https://github.com/influxdata/influxdb-python) does not support this parameter binding
- [The Java client](https://github.com/influxdata/influxdb-java) does support parameter binding, but for a project I needed the possibility to set also field names in the WHERE clause, as well as LIMIT and OFFSET, which came from a HTTP request and could not be trusted. Also I needed to set the field names dynamically because a user should choose the field names, which could have different names and types. Therefor I needed to know the field types to check the user input

# How does it work

# Example
If you know the type that the parameter should have

```python
query = "SELECT * FROM \"measurement\" WHERE field > ? AND field = ? AND field < ? AND field > ?"

query_builder = QueryBuilder(query, influxdb_url, db)
   
# String
user_input = "untrusted_string"
query_builder.setString(user_input)

# Integer
user_input = 0
query_builder.setInt(user_input)

# Integer that comes in as string, for example if coming as query parameter
user_input = "0" 
query_builder.setInt(user_input)

# Float 
user_input = 1.0
query_builder.setFloat(user_input)

# If you dont know the type of a field
user_input = "untrusted_string"

```

If you dont know the type of a field and want to add field names and field values static
```python
query = "SELECT * FROM \"measurement\" WHERE field > ?"

query_builder = QueryBuilder(query, influxdb_url, db)
   
user_input_field_value = "untrusted_string"

query_builder.set_field_value("field", user_input_field_value)
```

If you dont know the type of a field and want to add field names and field values dynamically
```python
query = "SELECT * FROM \"measurement\" WHERE ? > ?"

query_builder = QueryBuilder(query, influxdb_url, db)
   
user_input_field_value = "untrusted_string"
user_input_field_name = "untrusted_string"

query_builder.set_field_value(user_input_field_name, user_input_field_value, measurement_id)

```
