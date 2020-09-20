import boto3
import time
aws_con=boto3.session.Session(profile_name="rakhi")
ec2_con=aws_con.client(service_name="ec2",region_name="us-east-1")

response=ec2_con.describe_instances(InstanceIds=["i-015c5555c7675b7ff","i-03ddaaf3cf3bbd7ee","i-0cc6b5d17ba9149e5"])

for each in response['Reservations']:
    for each_instance in each['Instances']:
        print(each_instance['PrivateIpAddress'])

