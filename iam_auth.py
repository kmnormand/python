from collections import defaultdict
import boto3

user_list = group_list = []
user_dict = defaultdict(list)
group_dict = defaultdict(list)

client = boto3.client('iam')

response = client.get_account_authorization_details(
    Filter = ["User", "Group"]
)

# print(response)

user_list = [x['UserName'] for x in response['UserDetailList']]
print(user_list)
for user in response['UserDetailList']:
    username = user['UserName']
    if (len(user['UserName']['AttachedManagedPolicies'])) !=0:
        managed_policies = user['UserName']['AttachedManagedPolicies']
        user_dict[username].append(managed_policies)
    # print(user)

print(user_dict)
group_list = [x['GroupName'] for x in response['GroupDetailList']]
print(group_list)
