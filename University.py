class University:
    def __init__(self, departments, courses, students, bankaccounts):
        self.departments = departments
        self.courses = courses
        self.students = students
        self.bankaccounts = bankaccounts
        
    def city(self):
        print(f"I am a student in {self.departments} and I choose {self.courses}.")
        
class Bankaccounts:
    def __init__(self, fees, students):
        self.fees = fees  
        self.students = students
        
bankaccounts = Bankaccounts("40,000", "1")
university = University("Old engineering building", "software engineering", "50", bankaccounts)
university.city()
print(university.departments, university.courses, university.students, university.bankaccounts.students)

bankaccounts1 = Bankaccounts("25000", "2")        
university1 = University("New engineering building", "Computer science", "40", bankaccounts1)
print(university1.departments, university1.courses, university1.students, university.bankaccounts.fees)

