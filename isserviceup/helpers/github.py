import requests
from isserviceup.config import config


def get_access_token(code):
    params = {
        'client_id': config.GITHUB_CLIENT_ID,
        'client_secret': config.GITHUB_CLIENT_SECRET,
        'code': code,
    }
    headers = {
        'Accept': 'application/json',
    }
    result = requests.post('https://github.com/login/oauth/access_token', params=params, headers=headers)
    return result


def get_user_info(access_token):
    params = {
        'access_token': access_token,
    }
    data = requests.get('https://api.github.com/user', params=params)
    return data
