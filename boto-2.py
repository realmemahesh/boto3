import boto3
import boto3.session

aws = boto3.session.Session(profile_name="boto")
ec2 =  aws.client("ec2")

responce = ec2.run_instances(
    IamInstanceProfile={
        'Name': 'dev-ec2'
    }
    MaxCount = 
    MinCount = 
)
