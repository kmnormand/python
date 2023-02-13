import boto3

# client = boto3.client('sts')

response = boto3.client('sts').get_caller_identity()['Account']

print(response)
