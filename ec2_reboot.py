import boto3
import time
aws_con=boto3.session.Session(profile_name="rakhi")
ec2_con=aws_con.client(service_name="ec2",region_name="us-east-1")

print("Rebooting the instances")

my_inst=ec2_con.reboot_instances(InstanceIds=["i-015c5555c7675b7ff","i-03ddaaf3cf3bbd7ee","i-0cc6b5d17ba9149e5"])