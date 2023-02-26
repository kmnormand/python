from collections import defaultdict
import boto3

user_list = group_list = []
user_dict = defaultdict(list)
group_dict = defaultdict(list)

client = boto3.client('iam')

response = client.get_account_authorization_details(
    Filter = ["User", "Group"]
)

user_list = [x['UserName'] for x in response['UserDetailList']]
print(user_list)
for user in response['UserDetailList']:
    username = user['UserName']
    if user.get("AttachedManagedPolicies"):
        user_dict[username].append(user.get("AttachedManagedPolicies"))
    else:
        print("Empty Managed Policy")

print(user_dict)
group_list = [x['GroupName'] for x in response['GroupDetailList']]
print(group_list)
