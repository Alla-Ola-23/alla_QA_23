import requests


class GitHub:
    def get_user(self, username):
        #один метод , який приймає username як параметр і передає його до урл адреси
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    

    

