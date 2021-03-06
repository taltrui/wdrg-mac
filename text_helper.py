from colorama import Fore, Style


def print_header(text):
    print(Fore.WHITE + Style.BRIGHT + text + Style.RESET_ALL)


def print_error(text):
    print(Fore.RED + Style.BRIGHT + '[ERROR] ' + text + Style.RESET_ALL)


def print_warning(text):
    print(Fore.YELLOW + '[WARNING] ' + text + Style.RESET_ALL)


def print_info(text):
    print(Fore.BLUE + Style.BRIGHT + '[INFO] ' + text + Style.RESET_ALL)


def print_success(text):
    print(Fore.GREEN + Style.BRIGHT + '[SUCCESS] ' + text + Style.RESET_ALL)


def new_line():
    print('\n')


def separator():
    print('----------------------------------')
