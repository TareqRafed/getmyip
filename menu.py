from pick import pick
from wapp import get_last_rec

def ask_contacts():
    title = 'Please choose your contact: '
    option, index = pick(get_last_rec(), title)
    print(option)
    print(index)

def ask_action():
    title = 'Please choose on of the following action: '
    option, index = pick(['Send IP', 'Send Custom Message', 'Send template message (requires configuration)'], title)