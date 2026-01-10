def can_acesss_api(user_role: str) -> bool:
    if user_role == "admin":
        return True
    elif user_role == "backend":
        return True
    else:
        return False
    
print(can_acesss_api(input("Enter your role: ")))


def data_filtering(scores: list) -> list:
    filtered_scores = []
    for score in scores:
        if score > 50:
            filtered_scores.append(score)
    return filtered_scores

print(data_filtering([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))



user_list = [
    {'username': 'alice', 'role': 'backend'},
    {'username': 'bob', 'role': 'frontend'},
    {'username': 'charlie', 'role': 'backend'},
    {'username': 'david', 'role': 'admin'},
    {'username': 'eve', 'role': 'admin'},
    {'username': 'frank', 'role': 'devops'}
]


def count_users_per_role(users: list) -> dict:
    backend_users= []
    for user in users:
        if user['role'] == 'backend':
            backend_users.append(user)
    return {
        'backend': len(backend_users),
    }

print(count_users_per_role(user_list))
