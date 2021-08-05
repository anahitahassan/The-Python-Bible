# 52: List Comprehensions

even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)

# 53/54: Project 7: Pig Latin Translator

# get sentence from user
original = input("Please enter a sentence that you want translated into Pig Latin: ").strip().lower()

# split sentence into words
words = original.split()
print(words)

# loop through words and convert to pig latin
new_words = []
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# stick words back together
output = " ".join(new_words)

# output the final string
print(output)

# 55: Section Review: review the pig latin translator program again.



