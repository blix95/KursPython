import math
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", "--principal", "--periods", "--interest")
args = parser.parse_args()
if len(args) < 4:
    print("Incorrect parameters")
else:
    pass
if (args.principal or args.payment or args.period or args.interest) < 0:
    print("Incorrect parameters")
else:
    pass

if args.type == "diff":
    if args.payment == True:
        print("Incorrect parameters")
    else:
        pass
    P = args.principal
    n = args.periods
    i = (args.interest / (12 * 100))
    for month in range(1,n + 1):
        D = (P / n) + i * (P - ((P * (m - 1)) / n))
        print("Month", month, ": payment is", D)
print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
choice = input()
if choice == "n":
    principal = int(input("Enter the loan principal:"))
    monthly = float(input("Enter the monthly payment:"))
    interest = float(input("Enter the loan interest:"))
    i = (interest / (12 * 100))
    n = math.log((monthly / (monthly - i * principal)), 1 + i)
    n = math.ceil(n)
    if n % 12 == 0 and n / 12 == 1:
        print("It will take 1 year to repay this loan!")
    elif n % 12 == 0 and n / 12 != 1:
        print("It will take", n / 12, "years to repay this loan!")
    else:
        print("It will take", n // 12, "years and", n % 12, "months to repay this loan!")
elif choice == "a":
    principal = int(input("Enter the loan principal:"))
    n = int(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))
    i = (interest / (12 * 100))
    monthly = principal * ((i * math.pow((1 + i), n)) / (math.pow((1 + i),n)-1))
    print("Your monthly payment =", math.floor(monthly) + 1,"!")
elif choice == "p":
    monthly = float(input("Enter the monthly payment:"))
    n = int(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))
    i = (interest / (12 * 100))
    principal = (monthly / ((i * math.pow((1 + i), n))/(math.pow((1 + i), n)-1)))
    print("Your loan principal =", math.floor(principal),"!")



