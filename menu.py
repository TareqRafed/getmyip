from pick import pick

def showMenu(options):
    title = 'Please choose your contact: '
    option, index = pick(options, title)
    print(option)
    print(index)