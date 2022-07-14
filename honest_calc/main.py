msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


def isfloat(n): #funkcja sprawdzajaca czy liczba jest typu float
    try:
        float(n)
        return True
    except ValueError:
        return False
while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split() #rozdzielanie wpisanego tekstu
    if (x.isnumeric() or isfloat(x)) and (y.isnumeric() or isfloat(y)): # sprawdzanie czy wpisane wartosci są liczbami
        if oper == "+" or oper == "-" or oper == "*" or oper == "/": #sprawdza czy wprowadzony operator jest poprawny
            break
        else:
            print(msg_2)
            continue
    else:
        print(msg_1)
        continue

