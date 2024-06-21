import boto3
import logging
import json
from datetime import datetime

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Log the received event
        logger.info("Received event: " + json.dumps(event, indent=2))

        # Get the source bucket name from the event
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        
        # Define the destination buckets
        destination_buckets = ['des_bucket1', 'des_bucket2']

        # List objects in the source bucket with the prefix 'assets/index-'
        response = s3.list_objects_v2(Bucket=source_bucket, Prefix='assets/index-')
        
        if 'Contents' not in response:
            logger.info('No objects found with prefix assets/index-')
            return

        # Filter and sort objects by last modified date
        objects = response['Contents']
        js_files = sorted([obj for obj in objects if obj['Key'].endswith('.js')], key=lambda x: x['LastModified'], reverse=True)
        css_files = sorted([obj for obj in objects if obj['Key'].endswith('.css')], key=lambda x: x['LastModified'], reverse=True)
        
        # Get the last two .js and .css files
        files_to_copy = js_files[:2] + css_files[:2]

        for file in files_to_copy:
            object_key = file['Key']
            copy_source = {'Bucket': source_bucket, 'Key': object_key}
            destination_key = f"assets/{object_key.split('/')[-1]}"

            for destination_bucket in destination_buckets:
                try:
                    logger.info(f'Copying {object_key} to {destination_bucket}/{destination_key}')
                    s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=destination_key)
                    logger.info(f'Successfully copied {object_key} to {destination_bucket}/{destination_key}')
                except Exception as e:
                    logger.error(f'Error copying {object_key} to {destination_bucket}/{destination_key}: {e}')

    except Exception as e:
        logger.error(f'Error processing event: {e}')

    return {
        'statusCode': 200,
        'body': 'Successfully processed the event'
    }
