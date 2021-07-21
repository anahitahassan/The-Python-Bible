# 26: PROJECT 3: Email Slicer - Part 1 - What are Slices?

word = "supercalifragilisticexpialidocious"
print(word[2])

# [0:end:step]
# 0 to the designated number, but DOES NOT INCLUDE IT
# step is just going by each element (by 1 elements, by 2 elements, ...)
print(word[0:5:1]) # super
print(word[5:9:2]) # cali, but since we're going by two, it's just cl
print(word[0:5:2]) # super, but since we're going by 2 (evens), it's just spr, since those are 0, 2, 4/ 

print(word[5::2]) # cuts off 5 from the beginning, then goes by every 2. 
print(word[::7]) # goes by 7. (0, 7, 14, 21, ...)

print(word[::-1]) # "1" would just go by one and repeat the entire thing. 
# but "-1" woudl cause it to go backwards. 


# 27: PROJECT 3: Email Slicer - Part 2 - Automated Slices
print(word[-2])

# What if I want a segment and I don't want to count?
cali_index = word.index("cali") # 5
fragi_index = word.index("fragi") # 9
new_word = word[cali_index:fragi_index]
print(new_word)
# so what happens here is everything before 5 (excluding 5) is deleted, and everything after 9 (including 9) is deleted too
# the first number is excluded, the last number is included. 

print(word [word.index("fragilistic") : word.index("exp")] )
print(word [word.index("fragilistic") : word.index("e")] )
# this second one won't work since there is an "e" before the frag part. 