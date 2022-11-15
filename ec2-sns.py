import boto3

region = 'us-east-1'
instances = ['i-0bee46cc060afd596','i-02bb1a43da72e25c7','i-01a0d3a6ebce41216']
ec2 = boto3.client('ec2', region_name=region)
sns = boto3.client('sns')


def lambda_handler(event, context):
    print('Stopping instances')
    ec2.stop_instances(InstanceIds=instances)
   

def lambda_handler(event, context):
    topic_arn = 'arn:aws:sns:us-east-1:604199317070:Demo-EC2-Alerts'
    message = f"your server  {instances} is down"
    sns.publish(TopicArn=topic_arn,Message=message)
