import boto3
import time
aws_con=boto3.session.Session(profile_name="rakesh")
ec2_inst_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_inst_cli=aws_con.client(service_name="ec2",region_name="us-east-1")

my_inst=ec2_inst_re.Instance("i-0f3629dc3be738682")
print("Starting given instance........")
my_inst.start()
my_inst.wait_until_running()
print("Your instance is up and running")