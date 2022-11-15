import boto3
ec2 = boto3.client("ec2")
sns = boto3.client("sns")

def lambda_handler(event, context):
    print(event)
    ec2_instance_id = event['detail']['instance-id']
    print(ec2_instance_id)
    msg = f"Instance with ID {ec2_instance_id} is stopping"
    
    sns.publish(
            TopicArn = 'arn:aws:sns:us-east-1:604199317070:Demo-EC2-Alerts',
            Message=msg,
            Subject='EC2 Instance Alerts -BCReddy Devops',
        )
# start instance 
ec2.start_instances(
    InstanceIds=[
        ec2_instance_id
    ]
    
)
