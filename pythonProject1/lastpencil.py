

number = input("How many pencils would you like to use:")
while True:
    if isinstance(number, int) or number.isnumeric():
        number = int(number)
        if number != 0:
            name = input("Who will be the first (John, Jack): ")
            if name == "John" or name == "Jack":
                print("|" * number)
                print(name, "turn:")
                while number > 0:
                    i = int(input())
                    number = number - i
                    print("|" * number)
                    if name == "John" and number > 0:
                        name = "Jack"
                        print(name, "turn:")

                    elif name == "Jack" and number > 0:
                        name = "John"
                        print(name, "turn:")
            else:
                print("Choose between John and Jack")
                name = input()
        else:
            print("The number of pencils should be positive")
            number = input()
    else:
        print("The number of pencils should be numeric")
        number = input()


