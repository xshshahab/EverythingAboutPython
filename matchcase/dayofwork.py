day = input("Enter a day (e.g., Monday, Tuesday): ")

match day:
    case "Monday" | "monday":
        print("Start of the work week!")
    case "Tuesday" | "tuesday":
        print("It's a regular weekday")
    case "Wednesday" | "wednesday":
        print("Hump day!")
    case "Thursday" | "thursday":
        print("Almost to the weekend!")        
    case "Saturday" | "saturday" | "Sunday" | "sunday":
        print("It's the weekend!")
    case _:
        print("It's an invalid day.")
