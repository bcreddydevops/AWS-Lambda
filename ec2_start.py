import boto3
region = 'us-east-1'
instances = ['i-0bee46cc060afd596','i-02bb1a43da72e25c7','i-01a0d3a6ebce41216']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    print('Starting instances')
    ec2.start_instances(InstanceIds=instances)
