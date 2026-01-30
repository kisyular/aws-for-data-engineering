import boto3
from datetime import datetime

def main():
    print("GLUE JOB STARTED")
    print(f"Timestamp: {datetime.now().isoformat()}")

    # List files in the bucket (proves S3 access works)
    s3 = boto3.client('s3')
    bucket = 'real-learn-s3'

    response = s3.list_objects_v2(Bucket=bucket, MaxKeys=5)

    print(f"First 5 objects in {bucket}:")
    for obj in response.get('Contents', []):
        print(f"- {obj['Key']}")

    print("GLUE JOB COMPLETED SUCCESSFULLY")

if __name__ == '__main__':
    main()
