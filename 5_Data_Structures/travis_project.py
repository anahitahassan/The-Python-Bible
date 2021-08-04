# 38/39/40: PROJECT 4: Travis the Ridiculous Security System

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

list = [1, 4, 2, 6, 2, 9]
print(10 in list)
print(1 in list)

while True:
   print("Hi! My name is Travis")
   name = input("What is your name?: ").strip().capitalize()

   if name in known_users:
       print("Hello {}!".format(name)) 
       remove = input("Would you like to be removed from the system (y/n)?: ").lower()
       if remove == "y": 
           print(known_users)
           known_users.remove(name)
           print(known_users)
   else:
        print("Hmmmm I don't think I've met you yet {}.".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)

# strings are case sensitive so we can't put 'alice' it needs to be "Alice" to be recognized. 
# you can use the capitalize method to make it capitalized. 