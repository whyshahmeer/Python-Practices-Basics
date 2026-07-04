DBZ = ["Goku", "Vegeta", "Gohan", "Trunks"]

print("Original List:")
print(DBZ)

DBZ.append("Piccolo")

DBZ.insert(0, "Krillin")


DBZ.extend(["Android 17", "Android 18"])

print("\nAfter append(), insert(), and extend():")
print(DBZ)

DBZ.remove("Krillin")

print("\nAfter remove('Krillin'):")
print(DBZ)

removed_DBZ = DBZ.pop(2)

print("\nRemoved Character:")
print(removed_DBZ)

print("\nList after pop():")
print(DBZ)

DBZ.append("Goku")

print("\nNumber of Goku:")
print(DBZ.count("Goku"))


DBZ.sort()

print("\nSorted List:")
print(DBZ)

DBZ.reverse()

print("\nReversed List:")
print(DBZ)

copied_list = DBZ.copy()

print("\nCopied List:")
print(copied_list)


print("\nTotal Characters:")
print(len(DBZ))

DBZ.clear()

print("\nAfter clear():")
print(DBZ)