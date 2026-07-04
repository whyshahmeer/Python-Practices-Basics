letter = input("Enter a single letter: ").upper()

match letter:
    case "A" | "E" | "I" | "O" | "U":
        print(f"{letter} is a Vowel.")

    case _:
        print(f"{letter} is a Consonant.")