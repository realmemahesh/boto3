import boto3
import schedule
import time
from datetime import datetime

# Initialize Boto3 clients
rds_client = boto3.client('rds')
s3_bucket = "your-s3-bucket-name"
rds_instance_id = "your-rds-instance-id"

# Function to create RDS snapshot
def create_rds_snapshot():
    # Define snapshot identifier (with timestamp to make it unique)
    snapshot_identifier = f"rds-backup-{rds_instance_id}-{datetime.now().strftime('%Y-%m-%d-%H-%M')}"

    # Create RDS snapshot
    print(f"Creating snapshot for RDS instance {rds_instance_id}...")
    try:
        rds_client.create_db_snapshot(
            DBSnapshotIdentifier=snapshot_identifier,
            DBInstanceIdentifier=rds_instance_id
        )
        print(f"Snapshot {snapshot_identifier} created successfully.")
        export_snapshot_to_s3(snapshot_identifier)
    except Exception as e:
        print(f"Error creating snapshot: {str(e)}")

# Function to export RDS snapshot to S3
def export_snapshot_to_s3(snapshot_identifier):
    export_task_identifier = f"export-task-{snapshot_identifier}"
    print(f"Exporting snapshot {snapshot_identifier} to S3...")

    try:
        rds_client.start_export_task(
            ExportTaskIdentifier=export_task_identifier,
            SourceArn=f"arn:aws:rds:<region>:<account-id>:snapshot:{snapshot_identifier}",
            S3BucketName=s3_bucket,
            IamRoleArn="arn:aws:iam::<account-id>:role/<IAM-role-with-export-permissions>",
            KmsKeyId="arn:aws:kms:<region>:<account-id>:key/<kms-key-id>"
        )
        print(f"Export task {export_task_identifier} started successfully.")
    except Exception as e:
        print(f"Error exporting snapshot: {str(e)}")

# Schedule the task to run daily at 10 PM
schedule.every().day.at("22:00").do(create_rds_snapshot)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for the next check
