def evaluate_week(week):
    
    match week.upper():
        case 'M':
            return "Monday"
        case 'T':
            return "Tuesday"
        case 'W':
            return "Wednesday"
        case 'T':
            return "Thursday"
        case 'F':
            return "Friday"
        case _:
            return "Invalid"

week_day = input("Enter day you love: ")
print(evaluate_week(week_day))
