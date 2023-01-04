def color(suit):
    if suit == "♣" or suit == "♠": return ("\u001b[30m" + suit + "\u001b[30m")
    elif suit == "♦" or suit == "♥": return ("\u001b[31m" + suit + "\u001b[30m")

def bold(string, col='black'):
    string = str(string)
    if col == 'black':
        return "\033[0m\033[1\033[29;1m" + string + "\033[0m"
    elif col == "red":
        return "\033[0m\033[1;31m" + string + "\033[0m"

def black(string):
    string = str(string)
    return "\u001b[30m" + string + "\u001b[30m"

def red(string):
    string = str(string)
    return "\u001b[31m" + string + "\u001b[30m"

def cyan(string):
    string = str(string)
    return "\u001B[36m" + string + "\u001B[30m"

def green(string):
    string = str(string)
    return "\u001B[32m" + string + "\u001B[30m" 

def yellow(string):
    string = str(string)
    return "\u001B[33m" + string + "\u001B[30m"

