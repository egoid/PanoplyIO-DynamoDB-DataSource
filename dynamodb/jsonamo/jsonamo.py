import subprocess
import boto3

# Exports Tables in DynamoDB to a ./tables/{TableName}.json
def export_tables(_aws_key , _aws_secret):

  client = boto3.client('dynamodb')

  AWS_KEY = _aws_key
  AWS_SECRET = _aws_secret

  tables = client.list_tables(
      ExclusiveStartTableName='string',
      Limit=200
  )

  for TABLE_NAME in tables.TableNames:
    table_export = subprocess.check_output(['./dynamo_to_json.sh' , AWS_KEY , AWS_SECRET , TABLE_NAME ])

  return tables.TableNames

# Cleans up ./tables/*.json
def cleanup_tables():
  subprocess.check_output(['./clean_up_tables.sh'])  
