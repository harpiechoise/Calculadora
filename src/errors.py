from colorama import Fore, Style


class Error:
    def __init__(self, desc, message):
        self.desc = desc
        self.message = message

    def show_meeesage(self):
        print(Fore.RED +
              f"{self.desc}: {self.message}" + Fore.RESET)
