import urllib.request

def get_ip():
    print('Getting That IP...')
    # Get external IPV4 address from aws
    return urllib.request.urlopen('https://checkip.amazonaws.com/').read().decode('utf8')