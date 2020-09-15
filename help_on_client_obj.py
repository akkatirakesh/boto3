import boto3
aws_mag_con=boto3.session.Session(profile_name="rakesh")
client=aws_mag_con.client(service_name="iam", region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="us-east-1")
s3_con_cli=aws_mag_con.client(service_name="s3", region_name="us-east-1")
response=client.list_users()
for each_item in response['Users']:
    print(each_item)
responc=ec2_con_cli.describe_instances()
for each_item in responc['Reservations']:
    for each_instance in each_item['Instances']:
        print(each_instance['InstanceId'])
    print('----------------------------')

resp=s3_con_cli.list_buckets()
print(resp)