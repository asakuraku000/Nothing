
import time
import os
import sys

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# ASCII art for "HAPPY NEW YEAR"
happy = """
 ██░ ██  ▄▄▄       ██▓███   ██▓███ ▓██   ██▓
▓██░ ██▒▒████▄    ▓██░  ██▒▓██░  ██▒▒██  ██▒
▒██▀▀██░▒██  ▀█▄  ▓██░ ██▓▒▓██░ ██▓▒ ▒██ ██░
░▓█ ░██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▄█▓▒ ▒ ░ ▐██▓░
░▓█▒░██▓ ▓█   ▓██▒▒██▒ ░  ░▒██▒ ░  ░ ░ ██▒▓░
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒▓▒░ ░  ░▒▓▒░ ░  ░  ██▒▒▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░▒ ░     ░▒ ░     ▓██ ░▒░ 
 ░  ░░ ░  ░   ▒   ░░       ░░       ▒ ▒ ░░  
 ░  ░  ░      ░  ░                   ░ ░     
                                     ░ ░     
"""

new_year = """
███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗███████╗ █████╗ ██████╗ 
████╗  ██║██╔════╝██║    ██║    ╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗
██╔██╗ ██║█████╗  ██║ █╗ ██║     ╚████╔╝ █████╗  ███████║██████╔╝
██║╚██╗██║██╔══╝  ██║███╗██║      ╚██╔╝  ██╔══╝  ██╔══██║██╔══██╗
██║ ╚████║███████╗╚███╔███╔╝       ██║   ███████╗██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
"""

colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m'
}

def print_colored(text, color):
    print(f"{colors[color]}{text}{colors['reset']}", end='')

def animate_text():
    color_list = list(colors.keys())[:-1]  # Exclude 'reset'
    try:
        while True:
            for color in color_list:
                clear_screen()
                print_colored(happy, color)
                print_colored(new_year, 'yellow')
                print("\n" + " " * 30 + "Press Ctrl+C to exit")
                time.sleep(0.5)
    except KeyboardInterrupt:
        clear_screen()
        print("Happy New Year! 🎉")
        sys.exit(0)

if __name__ == "__main__":
    animate_text()