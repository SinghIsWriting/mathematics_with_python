import colorama
from colorama import Fore
colorama.init(autoreset=True)

def factorial_of_number(num):
        fact = 1
        while num > 0:
                fact *= num
                num -= 1
        return fact

def show():
        print(f"\n {Fore.CYAN}********** The factorial of a natural number n "+"**********\n")
        try:
                num = int(input("Enter a number n: "))
                if num <= 0:
                        print(f"{Fore.RED}Please enter a positive number !!!\n")
                else:
                        print(f"{Fore.GREEN}Result:", factorial_of_number(num))
                        print()
        except (ValueError, SyntaxError):
                print(f"\n{Fore.RED}Invalid input!")
                print("Usage: Enter a natural number.\n")

if __name__ == "__main__":
        show()
