def ask(prompt,retry=5,reminder = 'Try again!!'):
    """TODO: Docstring for ask.

    :arg1: TODO
    :returns: TODO

    """
    while True:
        reply = input(prompt)
        if reply in {'y','ye','haw','yes'}:
            return True
        if reply in {'n','no','neh','nahh','nope'}:
            return False
        retry = retry - 1
        if retry < 0:
            raise ValueError('Invalid response')
        print(reminder)

x = ask('Type Y or N\n')
print(x)

