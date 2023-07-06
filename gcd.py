import colorama
from colorama import Fore
colorama.init(autoreset=True)

# defining a function that takes two integers and returns GCD of them
def gcdOfTwoNumbers(x,y):
	if x<y:
		smaller = x
	else:
		smaller = y
	for i in range(1,smaller+1):
		if ((x%i == 0) and (y%i == 0)):
			gcd = i
	return gcd

def show():
	print(f"\n{Fore.CYAN}Greatest Common Divisor: gcd(8,12) = 4; 4 is the greatest divisor of 8 and 12.\n")
	try:
		a, b = input("Enter two numbers for GCD/HCF(e.g. 4 6): ").split()
		print(f"{Fore.GREEN} gcd({a},{b}) =",gcdOfTwoNumbers(int(a),int(b)))
	except:
		print(f"\n{Fore.RED}WARNING: Invalid input!")
		print("Usage: Enter two numbers separated with a space.\n")

if __name__ == "__main__":
	show()
