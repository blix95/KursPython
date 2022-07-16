msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

memory = 0
memory = float(memory)


def isfloat(n): #funkcja sprawdzajaca czy liczba jest typu float
    try:
        float(n)
        return True
    except ValueError:
        return False

def save_to_memory(answer): # funkcja zapisywania wyniku do pamieci
    global memory
    while True:

        if answer == "y":
            memory = result
            print(msg_5)
            answer = input()
            if answer == "y":
                return memory
            elif answer == "n":
                quit()
            else:
                continue
        elif answer == "n":
            print(msg_5)
            answer = input()
            if answer == "y":
                return memory
            elif answer == "n":
                quit()
            else:
                continue
        else:
            continue

def is_one_digit(v): # funkcja sprawdza czy liczba jest cyfrą  i jest typu int
    if -10 < v < 10 and int(v) == v:
        return True
    else:
        return False

def check(v1, v2, v3):

    msg = ""
    while True:

        if is_one_digit(v1) and is_one_digit(v2):
            msg = msg + msg_6

        if (v1 == 1 or v2 == 1) and v3 == "*":
            msg = msg + msg_7

        if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
            msg = msg + msg_8

        if msg != "":
            msg = msg_9 + msg
            print(msg)
            break

        else:
            break



while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split() #rozdzielanie wpisanego tekstu
    if x == "M":
        x = memory
        x = str(x)
    else:
        if y == "M":
            y = memory
            y = str(y)
    if (x.isnumeric() or isfloat(x)) and (y.isnumeric() or isfloat(y)): # sprawdzanie czy wpisane wartosci są liczbami
        x = float(x)
        y = float(y)
        if oper == "+" or oper == "-" or oper == "*" or oper == "/": #sprawdza czy wprowadzony operator jest poprawny
            check(x, y, oper)
            if oper == "+":
                result = x + y
                print(result)
                print(msg_4)
                answer = input()
                save_to_memory(answer)
            elif oper == "-":
                result = x - y
                print(result)
                print(msg_4)
                answer = input()
                save_to_memory(answer)
            elif oper == "*":
                result = x * y
                print(result)
                print(msg_4)
                answer = input()
                save_to_memory(answer)
            elif oper == "/" and y != 0:
                result = x / y
                print(result)
                print(msg_4)
                answer = input()
                save_to_memory(answer)
            else:
                print(msg_3)
                continue
        else:
            print(msg_2)
            continue
    else:
        print(msg_1)
        continue

