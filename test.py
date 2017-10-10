import unittest
import dynamodb


class TestDynamoDB(unittest.TestCase):

    def retrieve_tables(self):
        "Retrieves DynamoDB Tables"
      # s = dynamodb.read()

    def compiles_json(self):
        "Exports Tables to Json"

    def read_returns_list(self):
        "Read method returns unstructured data"        

     
# empty object, used for mocking
class Object(object): pass

# fire it up.
if __name__ == "__main__":
    unittest.main()
