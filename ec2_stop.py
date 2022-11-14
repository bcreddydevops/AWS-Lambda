import boto3
region = 'us-east-1'
instances = ['i-001e2d04e37ccde3b']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    print('Stopping instances')
    ec2.stop_instances(InstanceIds=instances)
