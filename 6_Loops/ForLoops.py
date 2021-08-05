# 50: For Loops

n = range(1, 11)
print(type(n))
print(n)

for number in range(1,11):
    print(number)


# count number of vowels and consonants.
vowels = 0
consonants = 0

for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))

# 51: For Loops part 2

students = {
    "male": ["Tom", "Charlie", "Harry"],
    "female": ["Anna", "Emily", "Eliza"]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)

