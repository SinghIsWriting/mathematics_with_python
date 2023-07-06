import gcd
import lcm
import mode
import factorial

options = '''
[1]     GCD of two numbers
[2]     LCM of two numbers
[3]     Mode
[4]     Factorial of a number
[5]     Factors of a number
[6]     Divisor of a number
[7]     Fibonacci series
[8]     Sum of Series
[9]     Play with Sets
[10]    Distance between two points
[11]    Solve Quadratic Equation
[12]    Exit
'''

print("\n\t***************** Welcome to Maths with Singh *****************\n\n")

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
    elif userOpt == "12" or userOpt.lower() == "exit":
        print("\nThanks for using this script :)")
        break

