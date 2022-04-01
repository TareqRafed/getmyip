from pick import pick

def showMenu():
    title = 'Please choose your favorite programming language: '
    options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
    option, index = pick(options, title)
    print(option)
    print(index)