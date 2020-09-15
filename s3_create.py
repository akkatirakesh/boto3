import boto3
aws_mag_con=boto3.session.Session(profile_name='rakesh')
s3_con=aws_mag_con.client('s3')

s3_con.create_bucket(Bucket='rakhi143245')