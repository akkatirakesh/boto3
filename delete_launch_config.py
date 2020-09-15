import boto3

aws_mag_con=boto3.session.Session(profile_name="rakesh")
ec2_con=aws_mag_con.client('autoscaling')

response = ec2_con.delete_launch_configuration(LaunchConfigurationName='example')
print(response)

