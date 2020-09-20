import boto3
aws_mag_con=boto3.session.Session(profile_name='rakesh')
dynamodb=aws_mag_con.client('dynamodb')
response=dynamodb.put_item(
TableName='Employee',
Item={
          'Employee_ID':'100',
          'Employee_Name':'Rakesh'
       
     }   
)