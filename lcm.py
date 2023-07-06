import colorama
from colorama import Fore
colorama.init(autoreset=True)

# defining a function that takes two integers as parameter and returns the lcm
def lcmOfTwoNumbers(x,y):
	if x<y:
		greater = y
	else:
		greater = x
	lcm = greater

	while True:
		if greater%x == 0 and greater%y == 0:
			return greater
			break
		else:
			greater = greater + lcm

def show():
	print(f"{Fore.CYAN}Least Common Multiple of 4, 6 = 12; Here, 12 is the least common multiple of 4 and 6.\n")

	try:
		a, b= input("Enter two numbers for LCM(e.g. 4 6): ").split()
		print(f"{Fore.GREEN} LCM of {a} and {b} =",lcmOfTwoNumbers(int(a),int(b)))
	except:
		print(f"\n{Fore.RED}WARNING: Invalid input!")
		print("Usage: Enter two numbers separated with a space.\n")

if __name__ == "__main__":
	show()
