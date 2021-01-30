import pyfiglet
from random import *

strings = ["linux", "arch", "pcmr", "hello world", "smile", "lulw", "hi"]

word = randint(0, 6)

def output():
    string=pyfiglet.print_figlet(strings[word], colors='CYAN')
    return string
output()
