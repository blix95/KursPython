import math
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if args.type == "diff":
    if args.payment:
        print("Incorrect parameters")
    else:
        pass
    suma_wplat = 0
    P = args.principal
    n = args.periods
    i = (args.interest / (12 * 100)) #obliczamy nominal interest rate
    for month in range(1,n + 1): #iterujemy po miesiącach spłat
        D = (P / n) + (i * (P - ((P * (month - 1)) / n))) #obliczamy kwotę do spłaty w danym miesiącu
        suma_wplat += math.ceil(D)
        print("Month", month, ": payment is", math.ceil(D))
    print("Overpaymant = ", suma_wplat - P)
elif args.type == "annuity":

    if args.principal and args.payment and args.interest: #oblicznie czasu spłaty
        P = args.principal
        payment = args.payment #monthly
        i = (args.interest / (12 * 100))
        n = math.ceil((math.log((payment / (payment - i * P)), 1 + i)))
        if n % 12 == 0 and n / 12 == 1:
            print("It will take 1 year to repay this loan!")
        elif n % 12 == 0 and n / 12 != 1:
            print("It will take", n / 12, "years to repay this loan!")
        else:
            print("It will take", n // 12, "years and", n % 12, "months to repay this loan!")
    elif args.principal and args.periods and args.interest:
        P = args.principal
        n = args.periods
        i = (args.interest / (12 * 100))
        monthly = principal * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))
        print("Your monthly payment =", math.floor(monthly) + 1, "!")
    elif choice == "p":
        monthly = float(input("Enter the monthly payment:"))
        n = int(input("Enter the number of periods:"))
        interest = float(input("Enter the loan interest:"))
        i = (interest / (12 * 100))
        principal = (monthly / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
        print("Your loan principal =", math.floor(principal), "!")
