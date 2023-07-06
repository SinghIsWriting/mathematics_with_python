import colorama
from colorama import Fore
colorama.init(autoreset=True)

def mode(list):
	return max(set(list), key=list.count)

def frequency_of_mode(list, mode):
	frq = 0
	for i in list:
		if mode == i:
			frq += 1
	return frq

def show():
	print(f"{Fore.CYAN}********** Mode and Frequency of mode in list of numbers "+"**********\n\n")
	example_list = [5,8,5,8,8,6,5,6,5,6]
	print("Example:")
	print(example_list)
	print(f"{Fore.YELLOW}Total elements in list:",len(example_list))
	print(f"{Fore.GREEN}Mode:",mode(example_list))
	print(f"{Fore.CYAN}Frequency of Mode:",frequency_of_mode(example_list, mode(example_list)))
	print()
	print(f"{Fore.CYAN}-"*60)
	l = input("Enter the list elements: ").split()
	lst = []

	try:		
		for i in l:
			lst.append(int(i))
		print()
		print(lst)
		print(f"{Fore.YELLOW}Total elements in list:",len(lst))
		mod = mode(lst)
		freq = frequency_of_mode(lst, mod)
		modes = []
		for j in list(set(lst)):
			if frequency_of_mode(lst, j) == freq:
				modes.append(j)
		if freq <= 1:
			print(f"{Fore.GREEN}Mode:", "No mode found")
		else:
			if len(modes) > 1:
				print(f"{Fore.GREEN}Modes:",modes)
				print(f"{Fore.CYAN}Frequency of these Modes:",freq)
			else:
				print(f"{Fore.GREEN}Mode:",mod)
				print(f"{Fore.CYAN}Frequency of Mode:",freq)
		print()
	except:
		print(f"\n{Fore.RED}Invalid input!")
		print("Usage: Enter intger numbers separated with a space.\n")

if __name__ == "__main__":
	show()
