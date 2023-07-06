import colorama
from colorama import Fore
colorama.init(autoreset=True)

# defining a function that takes a number and returns a list of factors
def factors(num):
	lst = []
	for i in range(1,num+1):
		if num%i == 0:
			lst.append(i)
	return lst

def show():
	print(f"\n {Fore.CYAN}********** Factors of a natural number n "+"**********\n")
	try:
		num = int(input("Enter the number here: "))
		fact = factors(num)
		print(f"\n{Fore.CYAN}No. of factors =", len(fact))
		print(f"{Fore.GREEN}Factors:", fact)
		print()
	except (ValueError, SyntaxError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Enter a natural number.\n")

if __name__ == "__main__":
	show()
