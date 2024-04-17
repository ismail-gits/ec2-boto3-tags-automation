import boto3

def get_instance_ids(ec2_client):
    instance_ids = []
    
    reservations = ec2_client.describe_instances()
    for reservation in reservations['Reservations']:
        instances = reservation['Instances']
        for instance in instances:
            instance_ids.append(instance['InstanceId'])
    
    return instance_ids

def create_tags(ec2_client, instance_ids, key, value):
    ec2_client.create_tags(
    Resources=instance_ids,
    Tags=[
        {
            'Key': key,
            'Value': value
        },
    ]
    )
    
    
# Mumbai region
ec2_client_virginia = boto3.client('ec2', region_name='us-east-1')
instance_ids_virginia = get_instance_ids(ec2_client_virginia)
create_tags(ec2_client_virginia, instance_ids_virginia, 'environment', 'prod')

# # Ohio region
ec2_client_ohio = boto3.client('ec2', region_name='us-east-2')
instance_ids_ohio = get_instance_ids(ec2_client_ohio)
create_tags(ec2_client_ohio, instance_ids_ohio, 'environment', 'dev')