import requests, pprint, urllib
from urllib.parse import urljoin
from pprint import pprint

class VKUser:
    #OAUTH_API_BASE_URL = "https://api.vk.com/method/"
    #TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"
    #V = "5.124"

    def __init__(self, user_id, token, version):
        self.token = token
        self.user_id = user_id
        self.id = urljoin("http://vk.com/", str(self.user_id))
        self.v = version

    def __repr__(self):
        return self.id

    def __and__(self, other):
        get_friends = "https://api.vk.com/method/friends.getMutual"
        response = requests.get(get_friends, params={
            "access_token": self.token,
            "v": self.v,
            "source_uid": self.user_id,
            "target_uid": other.user_id,
            "order": "random"
        })
        return [VKUser(friends, self.token, self.v) for friends in response.json().get("response")]

def main():
    TOKEN = "a7449c0e2ee529ef62c4dfb3b8dbefeb96d67df420f3d5eb3d6eec4e865228de214bcfdbe2e7aacf6c630"
    V = "5.124"
    user1 = VKUser(199141051,TOKEN, V)
    user2 = VKUser(255455912,TOKEN, V)
    return print(user1 & user2), print(user1)

main()