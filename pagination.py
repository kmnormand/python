import boto3

groups =[]
client = boto3.client('ec2')
paginator = client.get_paginator('describe_security_groups')

response_iterator = paginator.paginate()
for page in response_iterator:
    groups.extend(page['SecurityGroups'])

group_list = [x['GroupId'] for x in groups]
print(group_list)
