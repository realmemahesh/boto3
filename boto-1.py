import boto3
import boto3.session

aws_management_console=boto3.session.Session(profile_name="boto")
iam_console = aws_management_console.resource("iam")

for each_user in iam_console.users.all():
    print(each_user.name)