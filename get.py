from urllib.parse import urlencode, urljoin

APP_ID = 7647484
OAUTH_API_BASE_URL = "https://oauth.vk.com/authorize"
REDIRECT_URI = "https://oauth.vk.com/blank.html"
SCOPE = "friends"
OAUTH_PARAMS = {
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    "response_type": "token",
    "client_id": APP_ID
}

print("?".join([OAUTH_API_BASE_URL, urlencode(OAUTH_PARAMS)]))