import requests

def get_github_user(username):
    headers = {"Authorization": "Bearer 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"}

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        print(f"Имя пользователя: {user_data['login']}")
        print(f"Имя: {user_data['name']}")
        print(f"Аватар: {user_data['avatar_url']}")
        print(f"Количество репозиториев: {user_data['public_repos']}")
        print(f"Локация: {user_data['location']}")
    else:
        print(f"Ошибка {response.status_code}: {response.text}")

if __name__ == "__main__":
    github_username = "exxs1deZY"
    get_github_user(github_username)
