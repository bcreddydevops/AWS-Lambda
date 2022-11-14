import boto3

sns = boto3.client("sns")

def lambda_handler(event, context):
    ec2_instance_id = event['detail']['instance-id']
    print(ec2_instance_id)
    msg = f"Instance with ID {ec2_instance_id} is stopping"
    
    sns.publish(
            TopicArn = 'arn:aws:sns:us-east-1:604199317070:BCReddy-EC2-Alerts',
            Message=msg,
            Subject='EC2 Instance Alerts -BCReddy Devops',
        )
