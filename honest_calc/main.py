msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

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
                break
            else:
                continue
        else:
            continue

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

