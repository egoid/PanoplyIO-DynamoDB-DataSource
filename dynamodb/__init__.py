import source

Stream = source.DynamoDb

def get_files(*args, **kwargs):
    return Stream(*args, **kwargs).get_files()
