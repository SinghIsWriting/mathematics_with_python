import colorama
from colorama import Fore
colorama.init(autoreset=True)
import gcd
import lcm
import mode
import factorial
import factors
import divisor
import fibonacci
import series
import sets
import distance
import quadratic_equations

options = '''
[1]     GCD of two numbers
[2]     LCM of two numbers
[3]     Mode and Frequency
[4]     Factorial of a number
[5]     Factors of a number
[6]     Check Divisor
[7]     Fibonacci series
[8]     Series
[9]     Play with Sets
[10]    Distance between two points
[11]    Solve Quadratic Equation
[12]    Exit
'''

print("\n\t*****************", f"{Fore.BLUE}Welcome to Maths with Singh", "*****************\n\n")

while(True):
    print(options)
    userOpt = input("Enter your options: ")
    if userOpt == "1" or userOpt.lower() == "gcd":
        gcd.show()
    elif userOpt == "2" or userOpt.lower() == "lcm":
        lcm.show()
    elif userOpt == "3" or userOpt.lower() == "mode":
        mode.show()
    elif userOpt == "4" or userOpt.lower() == "factorial":
        factorial.show()
    elif userOpt == "5" or userOpt.lower() == "factors":
        factors.show()
    elif userOpt == "6" or userOpt.lower() == "divisor":
        divisor.show()
    elif userOpt == "7" or userOpt.lower() == "fibonacci":
        while(True):
            print("[1]     Fibonacci series\n[2]     nth fibonacci number\n[3]     Back\n")
            usr = input("Choose: ")
            if usr == "1" or usr.lower() == "series":
                fibonacci.fibonacci_series()
            elif usr == "2" or usr.lower() == "number":
                print(f"\n {Fore.CYAN}++++++++++ Find nth fibonacci number "+"+++++++++++\n")
                try:
                    num = int(input("Enter index of fibonacci number: "))
                    n = fibonacci.fibonacci_number(num)
                    print(f"{Fore.GREEN}{num}th fibonacci number =", n)
                except (ValueError, SyntaxError):
                    print(f"\n{Fore.RED}Invalid input!")
                    print("Usage: Enter a natural number as index.")
                print()
            elif usr == "3" or usr.lower() == "back":
                break
            else:
                print(f"{Fore.YELLOW}WARNING: Invalid input!")
    elif userOpt == "8" or userOpt.lower() == "sum of series":
        while(True):
            print("[1]     Sum of n natural numbers\n[2]     nth Term of AP\n[3]     nth Term of GP\n[4]     Sum of finite AP\n[5]     Sum of finite GP\n[6]     Sum of infinite GP\n[7]     Back\n")
            usr = input("Choose: ")
            if usr == "1":
                series.sum_natural_numbers()
            elif usr == "2":
                series.nth_term_AP()
            elif usr == "3":
                series.nth_term_GP()
            elif usr == "4":
                series.sum_of_AP()
            elif usr == "5":
                series.sum_of_GP()
            elif usr == "6":
                series.sum_of_infinite_GP()
            elif usr == "7":
                break
            else:
                print(f"{Fore.YELLOW}WARNING: Invalid input!")
    elif userOpt == "9" or userOpt.lower() == "sets":
        print(f"\n{Fore.CYAN}*********** Set is a collection of well defined objects ************\n")
        s1 = input("Enter first set A: ")
        s2 = input("Enter second set B: ")
        l1 = set(s1.split())
        l2 = set(s2.split())

        print("\n[1]     Properties of set A\n[2]     Properties of set B\n[3]     Properties of both sets\n[4]     Union of both sets\n[5]     Intersection of both sets\n[6]     Difference of set A and B\n[7]     Difference of set B and A\n[8]     Symmetric Difference of set A and B\n[9]     Symmetric Difference of set B and A\n[10]    Number of Relations between both sets\n[11]    Number of Mappings from set A to B\n[12]    Number of Mappings from set B to A\n[13]    Back\n")

        while(True):
            usr = input("Choose: ")

            if usr == "1":
                print(f"{Fore.CYAN}Set A: ")
                sets.properties_of_set(l1)
            elif usr == "2":
                print(f"{Fore.CYAN}Set B: ")
                sets.properties_of_set(l2)
            elif usr == "3":
                print(f"{Fore.CYAN}Properties of both sets: ")
                sets.properties_of_two_sets(l1, l2)
            elif usr == "4":
                sets.union_of_sets(l1, l2)
            elif usr == "5":
                sets.intersection_of_sets(l1, l2)
            elif usr == "6":
                print(f"{Fore.CYAN}\nDifference of set A and B:")
                sets.difference_of_sets(l1, l2)
            elif usr == "7":
                print(f"{Fore.CYAN}\nDifference of set B and A:")
                sets.difference_of_sets(l2, l1)
            elif usr == "8":
                print(f"{Fore.CYAN}\nSymmetric Difference of set A and B:")
                sets.symmetric_difference_of_sets(l1, l2)
            elif usr == "9":
                print(f"{Fore.CYAN}\nSymmetric Difference of set B and A:")
                sets.symmetric_difference_of_sets(l2, l1)
            elif usr == "10":
                print(f"{Fore.BLUE}Total No. of Relations between both sets: ",(2**(len(l1)*len(l2))))
            elif usr == "11":
                print(f"{Fore.BLUE}Total No. of Mappings from set A to set B: ",len(l2)**len(l1))
            elif usr == "12":
                print(f"{Fore.BLUE}Total No. of Mappings from set B to set A: ",len(l1)**len(l2))
            elif usr == "13":
                break
            else:
                print(f"{Fore.YELLOW}WARNING: Invalid input!")
            print()
    elif userOpt == "10" or userOpt.lower() == "distance":
        distance.euclidean_distance()
    elif userOpt == "11" or userOpt.lower() == "quadratic equation":
        quadratic_equations.solve()
    elif userOpt == "12" or userOpt.lower() == "exit":
        print("\nThanks for using this script :)")
        break
    else:
        print(f"{Fore.YELLOW}WARNING: Invalid input!")

