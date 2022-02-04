import json
import boto3
import os

Ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
sns_client = boto3.client('sns')
waiter = client.get_waiter('instance_stopped')
Ids_EC2 = []
        
def lambda_handler(event, context):
    ec2_filter={"Name": "tag:test_id","Values": ["start-stop"]}
    for each in Ec2.instances.filter(Filters=[ec2_filter]):
        each.stop()
        Ids_EC2.append(each.instance_id)
        waiter.wait(InstanceIds = Ids_EC2)
        
    if Ids_EC2:
        snsArn = os.environ["SNSARN"]
        sns_client.publish(TopicArn=snsArn, Message='EC2 had been stopped', Subject='success')
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "EC2 Stopped"
        }),
    }