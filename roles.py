import boto3

client = boto3.client('iam')
not_found = []
response = client.list_roles()

role_list = [x['RoleName'] for x in response['Roles']]
role_id = [x['RoleId'] for x in response['Roles']]

my_roles = ['AthenaRoleProd', 'wormrole', 'Inspector-Lambda','qby-604']

for role in my_roles:
    if role not in role_list:
        not_found.append(role)
    else:
        print(f"Role exists for {role}")

print(not_found)

no_role = [role for role in my_roles if role not in role_list]

print(no_role)
