import boto3
import boto3.session
from pprint import pprint

aws_management_console = boto3.session.Session(profile_name="boto")
iam_console = aws_management_console.client('iam')

users = iam_console.list_users()['Users']

for user in users:
    print(user['UserName'])

