import boto3

aws_mag_con=boto3.session.Session(profile_name="rakesh")
ec2_con=aws_mag_con.client('autoscaling')

response = ec2_con.create_launch_configuration(LaunchConfigurationName='example', ImageId='ami-00514a528eadbc95b', InstanceType='t2.micro', IamInstanceProfile='ssmrole', SecurityGroups=[
        'sg-5839f801'])

print(response)

