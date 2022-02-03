import json
import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    ec2_filter={"Name": "tag:test_id","Values": ["start-stop"]}
    for each in ec2.instances.filter(Filters=[ec2_filter]):
        each.start()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
