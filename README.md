# influxdb_query_builder
Python query builder for InfluxDB, similar to JDBC for Java. Supports client side prepared statements

# Example
```python
query = "SELECT * FROM \"measurement\" WHERE field > ? AND field = ? AND field < ? AND field > ?"

query_builder = QueryBuilder(query)

# If you know the type that the parameter should have
    
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
```
