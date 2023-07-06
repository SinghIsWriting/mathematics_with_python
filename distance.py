import colorama
from colorama import Fore
colorama.init(autoreset=True)
import math

def euclidean_distance():
	print(f"{Fore.CYAN}********** Euclidean Distance between two points "+"**********\n")

	try:
		point1 = input("Enter the co-ordinate of first point: ").split()
		point2 = input("Enter the co-ordinate of second point: ").split()
		p = []
		q = []
		for i in point1:
			p.append(int(i))
		for j in point2:
			q.append(int(j))
		print(f"\nPoints are ({p[0]}, {p[1]}) and ({q[0]}, {q[1]})")
		# Calculate Euclidean distance
		print (f"{Fore.GREEN}Distances between both points:", round(math.dist(p, q), 3))
		print()
	except:
		print(f"{Fore.YELLOW}WARNING: Invalid input!")
		print("Usage: Please enter coordinates numbers separated with a space.\n")

if __name__ == "__main__":
	euclidean_distance()
