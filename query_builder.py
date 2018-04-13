class QueryBuilder():
    def __init__(self, query):
        self.query = query 

    def setString(self, value):
        escaped_string = self.escape(value)
        double_quoted_escaped_string = "\"{escaped_string}\"".format(escaped_string=escaped_string)
        self.query = self.query.replace("?", double_quoted_escaped_string, 1)
    
    def setInt(self, value):
        converted_integer = self.convert_to_int(value)
        if converted_integer:
            self.query = self.query.replace("?", converted_integer, 1)
    
    def setFloat(self, value):
        converted_float = self.convert_to_float(value)
        if converted_float:
            self.query = self.query.replace("?", converted_float, 1)

    def escape(self, value):
        pass 
    
    def convert_to_int(self, value):
        try:
            converted_integer = int(value)
            return converted_integer
        except ValueError as e:
            return False

    def convert_to_float(self, value):
        try:
            converted_float = float(value)
            return converted_float
        except ValueError as e:
            return False
    
    def check_field_value_type(self, field_name):
        pass

if __name__ == "__main__":
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