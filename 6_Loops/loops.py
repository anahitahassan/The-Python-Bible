# 47: Section Overview
#   - While loops
#   - For loops
#   - List Comprehensions

# 48: While Loops

# Example 1:
while False:
    print("Hello")

# Example 2:
i = 1
while i <= 10:
    print(i)
    i = i + 1

# Example 3:
list = []
while len(list) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    list.append(new_name)

print("Sorry list is full")
print(list)


# 49: Project 6: Baby Conversation Simulator

from random import choice

questions = ["Why is the sky blue?", "Why is there a face on the moon?", "Where are the dinosaurs?"]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()
