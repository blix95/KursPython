msg_ = ["Enter an equation",

        "Do you even know what numbers are? Stay focused!",

        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",

        "Yeah... division by zero. Smart move...",

        "Do you want to store the result? (y / n):",

        "Do you want to continue calculations? (y / n):",

        " ... lazy",

        " ... very lazy",

        " ... very, very lazy",

        "You are",

        "Are you sure? It is only one digit! (y / n)",

        "Don't be silly! It's just one number! Add to the memory? (y / n)",

        "Last chance! Do you really want to embarrass yourself? (y / n)"
        ]

memory = 0
memory = float(memory)

msg_index = 10


def isfloat(n):  # funkcja sprawdzajaca czy liczba jest typu float
    try:
        float(n)
        return True
    except ValueError:
        return False


def is_one_digit(v):  # funkcja sprawdza czy liczba jest cyfrą  i jest typu int
    if -10 < v < 10 and int(v) == v:
        return True
    else:
        return False


def save_to_memory(answer):  # funkcja zapisywania wyniku do pamieci
    global memory
    global msg_index
    msg_index = 10
    while True:

        if answer == "y":

            if is_one_digit(result):
                print(msg_[msg_index])
                answer = input()
                if answer == "y":
                    if msg_index < 12:
                        msg_index = msg_index + 1

                        continue
                    else:
                        memory = result

                        print(msg_[5])
                        answer = input()
                        if answer == "y":
                            return memory
                        elif answer == "n":
                            quit()
                        else:
                            continue
                        return memory
                elif answer == "n":
                    print(msg_[5])
                    answer = input()
                    if answer == "y":
                        return memory
                    elif answer == "n":
                        quit()
                    else:
                        continue
                else:
                    continue

            else:
                memory = result
                print(msg_[5])
                answer = input()
                if answer == "y":
                    return memory
                elif answer == "n":
                    quit()
                else:
                    continue


        elif answer == "n":
            print(msg_[5])
            answer = input()
            if answer == "y":
                return memory
            elif answer == "n":
                quit()
            else:
                continue
        else:
            continue


def check(v1, v2, v3):
    msg = ""
    while True:

        if is_one_digit(v1) and is_one_digit(v2):
            msg = msg + msg_[6]

        if (v1 == 1 or v2 == 1) and v3 == "*":
            msg = msg + msg_[7]

        if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
            msg = msg + msg_[8]

        if msg != "":
            msg = msg_[9] + msg
            print(msg)
            break

        else:
            break


while True:
    print(msg_[0])
    calc = input()
    x, oper, y = calc.split()  # rozdzielanie wpisanego tekstu
    if x == "M":
        x = memory
        x = str(x)
    if y == "M":
        y = memory
        y = str(y)
    if (x.isnumeric() or isfloat(x)) and (y.isnumeric() or isfloat(y)):  # sprawdzanie czy wpisane wartosci są liczbami
        x = float(x)
        y = float(y)
        if oper == "+" or oper == "-" or oper == "*" or oper == "/":  # sprawdza czy wprowadzony operator jest poprawny
            check(x, y, oper)
            if oper == "+":
                result = x + y
                print(result)
                print(msg_[4])
                answer = input()
                save_to_memory(answer)
            elif oper == "-":
                result = x - y
                print(result)
                print(msg_[4])
                answer = input()
                save_to_memory(answer)
            elif oper == "*":
                result = x * y
                print(result)
                print(msg_[4])
                answer = input()
                save_to_memory(answer)
            elif oper == "/" and y != 0:
                result = x / y
                print(result)
                print(msg_[4])
                answer = input()
                save_to_memory(answer)
            else:
                print(msg_[3])
                continue
        else:
            print(msg_[2])
            continue
    else:
        print(msg_[1])
        continue

