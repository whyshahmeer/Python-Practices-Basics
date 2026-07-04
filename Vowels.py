vowels = []
consonants = []

word = input("Enter a word: ")

for letter in word:
    if letter.isalpha():      
        if letter.lower() in "aeiou":          
            vowels.append(letter)
        else:
            consonants.append(letter)

print("Vowels List:", vowels)
print("Consonants List:", consonants)

print("\nTotal Vowels:", len(vowels))
print("\nTotal Consonants:", len(consonants))

print("\nType of vowels:", type(vowels))
print("\nType of consonants:", type(consonants))