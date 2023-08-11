import requests

def get_pull_requests(repo_owner, repo_name, state):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls?state={state}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def count_and_list_users(pull_requests):
    user_count = {}
    for pr in pull_requests:
        user = pr['user']['login']
        if user in user_count:
            user_count[user] += 1
        else:
            user_count[user] = 1
    
    sorted_users = sorted(user_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_users

if __name__ == "__main__":
    repo_owner = "hybridgroup"
    repo_name = "gobot"
    
    open_pulls = get_pull_requests(repo_owner, repo_name, "open")
    closed_pulls = get_pull_requests(repo_owner, repo_name, "closed")
    
    all_pulls = open_pulls + closed_pulls
    
    users = count_and_list_users(all_pulls)
    
    print("Usuários que fizeram pull requests:")
    for user, count in users:
        print(f"{user}: {count} pull requests")
