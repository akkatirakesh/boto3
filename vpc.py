import boto3
aws_mag_con=boto3.session.Session(profile_name="rakesh")
ec2=aws_mag_con.resource('ec2')
vpc=ec2.create_vpc(CidrBlock='10.0.0.0/16')
print(vpc.id)

subnet=ec2.create_subnet(CidrBlock='10.0.0.0/24', VpcId=vpc.id)
print(subnet.id)

sec_group=ec2.create_security_group(GroupName='python_vpc', Description='python_vpc_sg',VpcId=vpc.id)
sec_group.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=80, ToPort=80)
sec_group.authorize_egress(IpProtocol='tcp', FromPort=-1, ToPort=-1)
print(sec_group.id)

