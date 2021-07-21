# 24: Cool String Methods - Part 1

# .count() function returns the amount of the section from the string. 
number_of_e = "hello".count("e")
print(number_of_e)

number_of_l = "hello".count("l")
print(number_of_l)

# .lower() function makes everything lowercase
text = "Happy Birthday"
number_of_days = text.count("day")
print(number_of_days)
new_string = text.lower()
print(new_string)

# .upper() function makes everything uppercase
new_string = text.upper()
print(new_string)

# .capitalize() functions capitalizes only the first character
x = "BOOGIE NOW"
capitalized_text = x.capitalize()
print(capitalized_text) 

# .title() function capitalizes the frist character of each word. 
y = "happy birthday"
title = y.title()
print(title)

# .islower() function prints true is all characters are lowercase
a = "HELLO"
b = "hello"
print(a.islower()) # false
print(b.islower()) # true

# .isupper() function prints true is all characters are uppercase
print(a.isupper()) # true
print(b.isupper()) # false

