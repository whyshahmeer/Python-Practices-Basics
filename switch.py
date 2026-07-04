class GradeChecker:

    def check_grade(self, grade):
        grade = grade.upper()

        match grade:
            case "A":
                print("Grade: A")
                print("Excellent! Chocolates for you")

            case "B":
                print("Grade: B")
                print("Very Good! You are doing well")

            case "C":
                print("Grade: C")
                print("Good! You can still improve")

            case "D":
                print("Grade: D")
                print("Pass. Study harder next time")

            case "F":
                print("Grade: F")
                print("Fail. Don't give up, keep fighting")

            case _:
                print("Invalid Grade! Please enter A, B, C, D, or F.")


student = GradeChecker()

grade = input("Enter your grade (A-F): ")

student.check_grade(grade)