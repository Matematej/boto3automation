import json
import boto3

ec2 = boto3.resource('ec2')

ec2_filter={'Name': 'teg:test_id','Values': ['start-stop']}
def lambda_handler(event, context):
    for each in ec2.instances.filter(Filters=[ec2_filter]):
        each.stop()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
