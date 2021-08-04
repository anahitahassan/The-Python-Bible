# 32: if Statements

# python immediately indents the next line.
# if I wrote False instead of true, it wouldn't print.
if True: 
    print("it worked!")

num1 = 100
num2 = 150

if num1 > num2:
    print("num1 is bigger than num2")
else:
    print("num1 is less than num2")

# what happens if num1 = num2?

num3 = 400
num4 = 400

if num3 > num4: 
    print("num3 is bigger than num4")
else: 
    print("num3 is less than num4")

# notice how the second statement was printed?

# HERE'S WHAT YOU ACTUALLY WANT TO DO: 

num5 = 500
num6 = 500

if num5 > num6:
    print("num5 is greater than num6")
elif num6 > num5:
    print("num6 is greater than num5")
else:
    print("both numbers are equal")