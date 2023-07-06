import colorama
from colorama import Fore
colorama.init(autoreset=True)

def fibonacci_number(index):
	if index == 1 or index == 2:
		return index - 1
	else:
		return fibonacci_number(index-1) + fibonacci_number(index-2)


def fibonacci_series():
	a = 0
	b = 1
	print(f"\n {Fore.CYAN}++++++++++ Find n terms of fibonacci sequence "+"+++++++++++\n")
	try:
		num = int(input("Enter the number of fibonacci sequence to print: "))

		if num <=0 :
				print(f"{Fore.RED}WARNING: Please enter a natural number!\n")
		elif num == 1:
			print(f"{Fore.GREEN}"+str(a))
		else:
			print(f"{Fore.GREEN}"+str(a)+" "+str(b), end=" ")
			for i in range(1,num+1):
				c = a+b
				a = b
				b = c
				print(f"{Fore.GREEN}"+str(c), end=" ")
	except (ValueError, SyntaxError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Please Enter a natural number.\n")
	print("\n")

if __name__ == "__main__":
	print(fibonacci_number(f))
	fibonacci_series()
