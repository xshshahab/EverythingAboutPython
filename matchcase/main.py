number = int(input("Enter a number: "))

match number:
    case 0:
        print("Case is 0")
    case 12:
        print("Case is running..")
    case _:
        print("No match found")