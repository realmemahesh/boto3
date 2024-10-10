import boto3
from pprint import pprint

ec2_obj = boto3.client('ec2')

for instance in ec2_obj.describe_instances()["Reservations"]:
    pprint(instance['Instances'][0]['InstanceId'])
    ec2_obj.terminate_instances(
    InstanceIds=[
       instance['Instances'][0]['InstanceId']
    ]
    )
