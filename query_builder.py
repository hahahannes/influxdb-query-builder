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
    