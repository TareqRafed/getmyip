#!./getmyipvenv/bin/python
import urllib.request
import pyperclip

def copy2clip(txt):
    pyperclip.copy(txt)

# Get external IPV4 address from aws
external_ip = urllib.request.urlopen('https://checkip.amazonaws.com/').read().decode('utf8')

copy2clip(external_ip)

print(f'Your ip {external_ip} is now copied to Clipboard')

