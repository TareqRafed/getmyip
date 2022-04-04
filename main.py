#!./getmyipvenv/bin/python
import pyperclip
import webbrowser
from get_ip import get_ip 
from menu import showMenu
from wapp import get_last_rec


def copy2clip(txt):
    pyperclip.copy(txt)

external_ip = get_ip()
copy2clip(external_ip)

print(f'Your ip {external_ip} is now copied to Clipboard')
print(f'######################')
showMenu(get_last_rec())


