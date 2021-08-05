# 43: Dictionaries

students = {}
students = {"Alice":25, "Bob":27, "Claire": 17, "Dan":21, "Emma":22}
print(students["Dan"])

students["Fred"] = 25
students['Alice'] = 26 # 1 year older now

del students["Fred"] # dropped out

print(students.keys())

a = list(students.keys())
print(a[2])

# Unlike List/Tuple, Dictionary doesn't have order
# To access and item, you need its corresponding key.

# 44: Dictionaries -- build a rough and ready database

studentData = {
    "Alice": ["ID0001", 26, "A"], 
    "Bob": ["ID0002", 27, "B"], 
    "Claire": ["ID0003", 17, "C"], 
    "Dan": ["ID0004", 21, "D"], 
    "Emma": ["ID0005", 22, "E"], 
}

print("Claire's grade: " + studentData["Claire"][2])
print("Emma's age: " + str(studentData["Emma"][1]))
print("Dan's ID: " + studentData["Dan"][0])

# but all that requires knowing 0 = id, 1 = age and 2 = grade. 

formalStudentData = {
    "Alice": {"id": "ID0001", "age": 26, "grade": "A"}, 
    "Bob": {"id": "ID0002", "age": 27, "grade": "B"}, 
    "Claire": {"id": "ID0003", "age": 17, "grade": "C"}, 
    "Dan": {"id": "ID0004", "age": 21, "grade": "D"}, 
    "Emma": {"id": "ID0005", "age": 22, "grade": "E"}, 
}

print("Claire's grade: " + formalStudentData["Claire"]["grade"])
print("Emma's age: " + str(formalStudentData["Emma"]["age"]))
print("Dan's ID: " + formalStudentData["Dan"]["id"])