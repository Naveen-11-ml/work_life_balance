# Import dependendcies
import config

# Import libary required
import boto3

s3client = boto3.client('s3')
s3client.download_file(config.BUCKET_NAME, config.BUCKET_KEY, config.DATA_PATH / "raw/lifestyle.csv")