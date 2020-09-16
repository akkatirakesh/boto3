import boto3

aws_mag_con=boto3.session.Session(profile_name="rakesh")
rds_con=aws_mag_con.client('rds')
response=rds_con.create_db_instance(AllocatedStorage=5,
    DBName='mydatabase',
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='mydbinstance',
    Engine='MySQL',
    MasterUsername='',
    MasterUserPassword='',
    VpcSecurityGroupIds=['sg-5839f801'],
    AvailabilityZone='us-east-1c',
    DBSubnetGroupName='test',
    BackupRetentionPeriod=20,
   
)

print(response)