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
import sum_of_series

options = '''
[1]     GCD of two numbers
[2]     LCM of two numbers
[3]     Mode
[4]     Factorial of a number
[5]     Factors of a number
[6]     Check Divisor
[7]     Fibonacci series
[8]     Sum of Series
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
            print("[1]     Sum of n natural numbers\n[2]     Sum of finite AP\n[3]     Sum of finite GP\n[4]     Sum of infinite GP\n[5]     Back\n")
            usr = input("Choose: ")
            if usr == "1":
                sum_of_series.sum_natural_numbers()
            elif usr == "2":
                sum_of_series.sum_of_AP()
            elif usr == "3":
                sum_of_series.sum_of_GP()
            elif usr == "4":
                sum_of_series.sum_of_infinite_GP()
            elif usr == "5":
                break
            else:
                print(f"{Fore.YELLOW}WARNING: Invalid input!")
    elif userOpt == "12" or userOpt.lower() == "exit":
        print("\nThanks for using this script :)")
        break
    else:
        print(f"{Fore.YELLOW}WARNING: Invalid input!")

