import boto3
aws_mag_con=boto3.session.Session(profile_name="rakesh")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name='us-east-1')
for each in ec2_con_cli.describe_volumes()['Volumes']:
    print(each['VolumeId'])
print('Deleting volume')
ec2_con_cli.delete_volume(VolumeId=each['VolumeId'])