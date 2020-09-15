import boto3
aws_mag_con=boto3.session.Session(profile_name='rakesh')
ec2_con=aws_mag_con.client('autoscaling')

response=ec2_con.delete_auto_scaling_group(AutoScalingGroupName='myasg', ForceDelete=True|False)