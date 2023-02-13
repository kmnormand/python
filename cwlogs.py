import boto3

client = boto3.client("logs")

response = client.describe_log_groups()

# print(response)

my_group_names = [x['logGroupName'] for x in response['logGroups']]

print(my_group_names)

for group in my_group_names:
    try:
        filters = client.describe_subscription_filters(
            logGroupName = group
        )
        if len(filters['subscriptionFilters']) > 0:
            print("Compliant")
        else:
            print("No subscription filters")
    except:
        print("No subscription for {}".format(group))