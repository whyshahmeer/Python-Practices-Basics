class University:
    def __init__(self, departments, students, security, exams, program):
        self.departments = departments
        self.students = students
        self.security = security
        self.exams = exams
        self.program = program

    def city(self):
        print("Bahawalpur City")


class Program:
    def __init__(self, subjects, professors):
        self.subjects = subjects
        self.professors = professors


program = Program("DSA", "Codebro")

university = University(
    "Software Engineering",
    45,
    "Strict Security",
    "10 March",
    program
)

print(
    university.departments,
    university.security,
    university.program.subjects
)

university.city()


program1 = Program("Python", "Lighter")

university1 = University(
    "Computer Science",
    55,
    "Normal Security",
    "29 June",
    program1
)

print(
    university1.students,
    university1.exams,
    university1.program.professors
)

university1.city()