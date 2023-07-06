import colorama
from colorama import Fore
colorama.init(autoreset=True)

def sum_natural_numbers():
	print(f"\n {Fore.CYAN}++++++++++ Sum of n Natural Numbers "+"+++++++++++\n")
	try:
		num = int(input("Enter number of natural numbers: "))
		temp = num
		sum = 0
		while num > 0:
			sum += num
			num -= 1
		print(f"{Fore.GREEN}Sum of {temp} natural numbers =", sum)
	except (ValueError, SyntaxError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Please enter a natural number.")
	print()

def nth_term_AP():
	print(f"\n {Fore.CYAN}++++++++++ nth Term of a finite Arithmatic Progression "+"+++++++++++\n")
	try:
		a = float(input("Enter the first term of AP: "))
		d = float(input("Enter the common difference of AP: "))
		n = int(input("Enter the nth term you want: "))
		term = (a + ((n-1) * d))
		print(f"\n{Fore.CYAN}{n}th term of the Series =", round(term, 3))
	except (ValueError, SyntaxError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Please enter a valid number.")
	print()

def nth_term_GP():
	print(f"\n {Fore.CYAN}++++++++++ nth Term of a finite Geomatric Progression "+"+++++++++++\n")
	try:
		a = float(input("Enter the first term of GP: "))
		r = float(input("Enter the common ratio of GP: "))
		n = int(input("Enter the nth term you want: "))
		term = (a * (r**(n-1)))
		print(f"\n{Fore.CYAN}{n}th term of the Series =", round(term, 3))
	except (ValueError, SyntaxError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Please enter a valid number.")
	print()

def sum_of_AP():
	print(f"\n {Fore.CYAN}++++++++++ Sum of a finite Arithmatic Progression "+"+++++++++++\n")
	try:
		a = float(input("Enter the first term of AP: "))
		d = float(input("Enter the common difference of AP: "))
		n = int(input("Enter the number of terms in AP: "))
		sum = (n/2)*(2*a + ((n-1) * d))
		print(f"\n{Fore.CYAN}Series: ", end="")
		for i in range(n-1):
			print(round(a, 2), end=", ")
			a = a + d
		print(a+d)
		print(f"{Fore.GREEN}Sum of AP =", round(sum, 3))		
	except (ValueError, SyntaxError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Please enter a valid number.")
	print()

def sum_of_GP():
	print(f"\n {Fore.CYAN}++++++++++ Sum of a finite Geomatric Progression "+"+++++++++++\n")
	try:
		a = float(input("Enter the first term of GP: "))
		r = float(input("Enter the common ratio of GP: "))
		n = int(input("Enter the number of terms in GP: "))
		sum = 0
		if r == 1:
			sum = n * a
		elif r < 1:
			sum = (a*(1 - r**n))/(1 - r)
		elif r > 1:
			sum = (a*(r**n - 1))/(r - 1)
		print(f"\n{Fore.CYAN}Series: ", end="")
		for i in range(n-1):
			print(round((a * (r**(i))), 2), end=", ")
		print(a*(r**(n-1)))
		print(f"{Fore.GREEN}Sum of GP =", round(sum, 3))	
	except (ValueError, SyntaxError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Please enter a valid number.")
	print()

def sum_of_infinite_GP():
	print(f"\n {Fore.CYAN}++++++++++ Sum of an infinite Geomatric Progression "+"+++++++++++\n")
	try:
		a = float(input("Enter the first term of GP: "))
		r = float(input("Enter the common ratio of GP: "))
		sum = 0
		if (r>=-1 and r<=1):
			sum = a/(1-r)
			print(f"\n{Fore.CYAN}Series: ", end="")
			for i in range(10):
				print(round((a * (r**(i))), 2), end=", ")
			print("...")
			print(f"{Fore.GREEN}Sum of GP =", round(sum, 3))
		else:
			print(f"\n{Fore.CYAN}Series: ", end="")
			for i in range(10):
				print(round((a * (r**(i))), 2), end=", ")
			print("...")
			print(f"{Fore.GREEN}Sum of GP =", "Series diverges")
	except (ValueError, SyntaxError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Please enter a valid number.")
	print()

if __name__ == "__main__":
	# sum_natural_numbers()
	# sum_of_AP()
	# sum_of_GP()
	# sum_of_infinite_GP()
	# nth_term_AP()
	nth_term_GP()
