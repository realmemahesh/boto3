# project to create and delete the s3 bucket with api gateway

import boto3


ec2_obj = boto3.client("ec2")

ec2_obj.run_instances(    
    ImageId='ami-0ebfd941bbafe70c6',
    MaxCount=2,
    MinCount=1,
    Monitoring={
        'Enabled': True
    }
    
)

