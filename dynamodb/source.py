import panoply
from jsonamo import jsonamo
import json
from conf import CONFIG
from panoply.errors import PanoplyException


class DynamoDb(panoply.DataSource):
    def __init__(self, *args, **kwargs):
        super(DynamoDb, self).__init__(*args, **kwargs)
        self.tables = jsonamo.export_tables(CONFIG.AWS_KEY , CONFIG.AWS_SECRET)

    def read(self, n=None):
        if len(self.tables) == 0:
            return None 

        content=[]
        for table_name in self.tables:
            file_name = "./tables/" + table_name + ".json"

            with open(file_name) as data_file:    
                data = json.load(data_file)
                content.append(data)

        return content

    def close(self):
        jsonamo.cleanup_tables()
        return None
