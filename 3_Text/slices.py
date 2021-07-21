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
