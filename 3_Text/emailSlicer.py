# 28: PROJECT 3: Email Slicer - Part 3 - Making the Slicer!

# get user email address
email = input("What is your email address? : ").strip()
    # strip gets rid of any spaces after the answer. 

# slice out user name
# example email: anahitahassa@gmail.com -> "@"
location_of_symbol = email.index("@")
everything_after_username = email[location_of_symbol::]
print(everything_after_username)

# slice domain name
username = email[0:location_of_symbol]
print(username)

# format message
output = "Your username is {} and your domain name is {}".format(username, everything_after_username)

# display output message
print(output)

# 29: Section Review
#     - Learned ways to make strings
#     - Fix broken strings
#     - Take in user input with input() function
#     - String concatenation and formatting
#     - Working with incompatible datatypes
#     - String methods
#     - Slices