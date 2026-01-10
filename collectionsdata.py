from collections import Counter
# Input: A list of user dictionaries
user_list = [
    {'username': 'alice', 'role': 'admin'},
    {'username': 'bob', 'role': 'user'},
    {'username': 'charlie', 'role': 'admin'},
    {'username': 'david', 'role': 'editor'},
    {'username': 'eve', 'role': 'user'},
    {'username': 'frank', 'role': 'user'}
]

def count_users_per_role(users):


    # Extract all the roles into a list
    roles = [user['role'] for user in users]
    
    # Use Counter to count the occurrences of each role
    role_counts = Counter(roles)
    
    # Convert the Counter object to a standard dict for the output
    return dict(role_counts)

# Calculate the counts
user_counts_by_role = count_users_per_role(user_list)

# Print the output
print(user_counts_by_role)
