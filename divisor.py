import colorama
from colorama import Fore
colorama.init(autoreset=True)

# defining a function that takes a number and returns a list of factors
def isDivisor(num, divisor):
    if num%divisor == 0:
        return True
    else:
        return False

def show():
    print(f"\n {Fore.CYAN}********** Check either a number divides another number "+"**********\n")
    try:
        num = int(input("Enter the number here: "))
        div = int(input("Enter the divisor here: "))
        if isDivisor(num, div):
            print(f"{Fore.GREEN}Yes!")
        else:
            print(f"{Fore.RED}No!")
        print()
    except (ValueError, SyntaxError):
        print(f"\n{Fore.RED}Invalid input!")
        print("Usage: Enter a natural number.\n")

if __name__ == "__main__":
	show()
