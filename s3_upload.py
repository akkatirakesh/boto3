import boto3
aws_mag_con=boto3.session.Session(profile_name='rakesh')
s3_con=aws_mag_con.client('s3')

s3_con.upload_file('s3.txt','rakhi143245','mys3.txt')