import colorama
from colorama import Fore
colorama.init(autoreset=True)

def minempty(s):
	if len(s) == 0:
		print(f"{Fore.GREEN}Minimum value of set=",f"{Fore.YELLOW}It's an empty set !!!")
	else:
		print(f"{Fore.GREEN}Minimum value of set=",min(s))

def maxempty(t):
	if len(t) == 0:
		print(f"{Fore.GREEN}Minimum value of set=",f"{Fore.YELLOW}It's an empty set !!!")
	else:
		print(f"{Fore.GREEN}Maximum value of set=",max(t))

def properties_of_set(st):
	print(st, f"\n{Fore.GREEN}Cardinality=",len(st),f",{Fore.GREEN}No. of subsets=",2**len(st))
	print(f"{Fore.GREEN}Minimum value of set=",min(st),f"\n{Fore.GREEN}Maximum value of set=",max(st))

def properties_of_two_sets(st1, st2):
	if st1.isdisjoint(st2):
		print(f"{Fore.MAGENTA}\nBoth are disjoint sets: ", "Yes")
	else:
		print(f"{Fore.MAGENTA}\nBoth are disjoint sets: ", "No")

	if st1.issubset(st2):
		print(f"{Fore.MAGENTA}First set is subset of second: ", "Yes")
	else:
		print(f"{Fore.MAGENTA}First set is subset of second: ", "No")
	
	if st2.isdisjoint(st1):
		print(f"{Fore.MAGENTA}Second set is subset of first: ", "Yes")
	else:
		print(f"{Fore.MAGENTA}Second set is subset of first: ", "No")
	
	if st1.issuperset(st2):
		print(f"{Fore.MAGENTA}First set is superset of second: ", "Yes")
	else:
		print(f"{Fore.MAGENTA}First set is superset of second: ", "No")
	
	if st2.isdisjoint(st1):
		print(f"{Fore.MAGENTA}Second set is superset of first: ", "Yes")
	else:
		print(f"{Fore.MAGENTA}Second set is superset of first: ", "No")

def union_of_sets(st1, st2):
	print(f"{Fore.CYAN}\nUnion of both sets:")
	print(st1 | st2)
	print(f"{Fore.GREEN}Cardinality = {len(st1 | st2)}",f",{Fore.GREEN}No. of subsets=",2**len(st1 | st2))
	minempty(st1 | st2)
	maxempty(st1 | st2)

def intersection_of_sets(st1, st2):
	print(f"{Fore.CYAN}\nIntersection of both sets:")
	print(st1 & st2)
	print(f"{Fore.GREEN}Cardinality = {len(st1 & st2)}",f",{Fore.GREEN}No. of subsets=",2**len(st1 & st2))
	minempty(st1 & st2)
	maxempty(st1 & st2)

def difference_of_sets(st1, st2):
	print(st1 - st2)
	print(f"{Fore.GREEN}Cardinality = {len(st1 - st2)}",f",{Fore.GREEN}No. of subsets=",2**len(st1 - st2))
	if len(st1 - st2) == 0:
		print(f"{Fore.GREEN}Minimum value of set=",f"{Fore.YELLOW}It's an empty set !!!")
		print(f"{Fore.GREEN}Maximum value of set=",f"{Fore.YELLOW}It's an empty set !!!")
	else:
		print(f"{Fore.GREEN}Minimum value of set=",min(st1 - st2),f"\n{Fore.GREEN}Maximum value of set=",max(st1 - st2))

def symmetric_difference_of_sets(st1, st2):
	print(st1 ^ st2)
	print(f"{Fore.GREEN}Cardinality = {len(st1 ^ st2)}",f",{Fore.GREEN}No. of subsets=",2**len(st1 ^ st2))
	if len(st1 ^ st2) == 0:
		print(f"{Fore.GREEN}Minimum value of set=",f"{Fore.YELLOW}It's an empty set !!!")
		print(f"{Fore.GREEN}Maximum value of set=",f"{Fore.YELLOW}It's an empty set !!!")
	else:
		print(f"{Fore.GREEN}Minimum value of set=",min(st1 ^ st2),f"\n{Fore.GREEN}Maximum value of set=",max(st1 ^ st2))

