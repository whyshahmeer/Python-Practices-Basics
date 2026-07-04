def evaluate_grade(grade):

    match grade.upper():
        case 'A':
            return "Excellent performance!"
        case 'B':
            return "Good job!"
        case 'C':
            return "Satisfactory."
        case 'D':
            return "Needs improvement."
        case 'F':
            return "Failed. Please seek assistance."
        case _: 
            return "Invalid grade entered."
        
user_grade = input("Enter your letter grade (A-F): ")
print(evaluate_grade(user_grade))