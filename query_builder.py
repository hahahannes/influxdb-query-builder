import requests 

class QueryBuilder():
    def __init__(self, query, url, db):
        self.query = query 
        self.url = url 
        self.db = db

    def setString(self, value):
        """
        Replace the first occurence of questionmark with the escaped string
        """
        escaped_string = self.escape(value)
        double_quoted_escaped_string = "\"{escaped_string}\"".format(escaped_string=escaped_string)
        self.query = self.query.replace("?", double_quoted_escaped_string, 1)
    
    def setInt(self, value):
        """
        Replace the first occurence of questionmark with the converted integer value
        """
        converted_integer = self.convert_to_int(value)
        if converted_integer:
            self.query = self.query.replace("?", converted_integer, 1)
    
    def setFloat(self, value):
        """
        Replace the first occurence of questionmark with the converted float value
        """
        converted_float = self.convert_to_float(value)
        if converted_float:
            self.query = self.query.replace("?", converted_float, 1)

    def escape(self, value):
        """
        Escape a string, which can be user input. Therefor quotes have to be escaped and then wrapped into own quotes. 
        """
        escape_map = [("\"","\\\""), ("'", "\'")]
        for escape_pair in escape_map:
            value = value.replace(escape_pair[0], escape_pair[1])
        return value

    def execute(self,query):
        response = requests.post(self.url, params='db={db}&q={query}'.format(db=self.db, query=query)).json()
        return response
    
    def convert_to_int(self, value):
        """
        Try to convert the value to integer. If it raises an exception, it was probably a malicious string.
        """
        try:
            converted_integer = int(value)
            return converted_integer
        except ValueError as e:
            return False

    def convert_to_float(self, value):
        """
        Try to convert the value to float. If it raises an exception, it was probably a malicious string.
        """
        try:
            converted_float = float(value)
            return converted_float
        except ValueError as e:
            return False
    
    def check_field_value_type(self, field_name, measurement): 
        """
        Get the type of a field, in order to convert user input, for example a integer that is formatted as a string from a query parameter
        """
        query = "SHOW FIELD KEYS FROM \"{measurement}\"".format(measurement=measurement)
        response = self.execute(query)
        fields = response["results"][0]["series"][0]["values"]
        for field in fields: 
            if field[0] == field_name:
                return field[1]
        return None 

    def set_field_value(self, field_name, field_value, measurement):
        type_of_field = self.check_field_value_type(field_name, measurement)
        if type_of_field is "string":
            escaped_string = self.escape(field_value)
            self.query = self.query.replace()
        elif type_of_field is "integer":
            converted_integer = self.convert_to_int(field_value)
        elif type_of_field is "float":
            converted_float = self.convert_to_float(field_value)
