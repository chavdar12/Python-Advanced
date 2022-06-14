from pyfiglet import figlet_format


def print_art(message):
    ascii_art = figlet_format(message)
    print(ascii_art)


print_art(input())

from pyfiglet import Figlet

f = Figlet()
print(f.renderText('text to render'))
