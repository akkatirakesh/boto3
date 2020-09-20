import boto3
aws_mag_con=boto3.session.Session(profile_name='rakesh')
dynamodb=aws_mag_con.client('dynamodb')

response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Employee_ID',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Employee_Name',
            'AttributeType': 'S'
        },
    ],
    TableName='Employee',
    KeySchema=[
        {
            'AttributeName': 'Employee_ID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Employee_Name',
            'KeyType': 'RANGE'
        },
    ],
 
    ProvisionedThroughput={
        'ReadCapacityUnits': 123,
        'WriteCapacityUnits': 123
    },
)

response=dynamodb.put_item(
TableName='Employee',
    Item={
          'Employee_ID':'100',
          'Employee_Name':'Rakesh'
         }
         