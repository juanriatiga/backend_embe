import boto3
dynamo_client = boto3.resource('dynamodb')
tabla = dynamo_client.Table('data_temp')
def save_data(payload):
    response = tabla.put_item(
    Item = payload
    )
    return(response)

def get_all_data():
    response = tabla.scan()
    data = response['Items']    
    #while 'lastEvaluatedKey' in response:
     #   response = tabla.scan(ExclusiveStarKey = response['LastEvaluatedKey'])
      #  data.extend(response[respnse'Items'])
    return(data)