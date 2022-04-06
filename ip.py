import urllib.request

def get_ip():
    print('Getting That IP...')
    # Get external IPV4 address from aws
    return urllib.request.urlopen('https://checkip.amazonaws.com/').read().decode('utf8')

def copy2clip(txt):
    pyperclip.copy(txt)

def give_user_ip():
    external_ip = get_ip()
    copy2clip(external_ip)

    print(f'Your ip {external_ip} is now copied to Clipboard')