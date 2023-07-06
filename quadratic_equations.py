import math
import cmath
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def solve():
	print(f"\n {Fore.CYAN}+++++ Find the roots of quadratic equation ax²+bx+c=0; a≠0 "+"+++++\n")
	try:
		a, b, *z= input("Enter the value of a, b and c : ").split()
		a = float(a)
		b = float(b)
		c = float(z[0])
		if a == 0:
			print(f"\n{Fore.YELLOW}WARNING: a must be a non-zero number!\n")
		else:
			d = (b**2) - (4*a*c)
			print()
			print(f"({a})x² + ({b})x + ({c}) = 0")
			print(f"{Fore.GREEN}Discriminant (b²-4ac) = ", round(d, 3))
			if d < 0:
				img_root1 = (-b + cmath.sqrt(d))/(2*a)
				img_root2 = (-b - cmath.sqrt(d))/(2*a)
				print(f"{Fore.MAGENTA}Roots are imaginary.")
				print(f"{Fore.GREEN}Roots are:",f"({-b}+√{d})/{(2*a)}", f"{Fore.GREEN}or", img_root1,f"{Fore.GREEN}and",f"({-b}-√{d})/{(2*a)}", f"{Fore.GREEN}or", img_root2)
			else:
				root1 = (-b + math.sqrt(d))/(2*a)
				root2 = (-b - math.sqrt(d))/(2*a)
				if d == 0:
					print(f"{Fore.YELLOW}Roots are real and identical.")
					print(f"{Fore.GREEN}Roots are",round(root1, 3),f"{Fore.GREEN}and",round(root2, 3))
				else:
					print(f"{Fore.BLUE}Roots are real.")
					print(f"{Fore.GREEN}Roots are",round(root1, 3),f"{Fore.GREEN}and",round(root2, 3))
			print()
	except (ValueError, SyntaxError, IndexError):
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Please enter three real numbers a, b and c separated with a space.\n")

if __name__ == "__main__":
	solve()