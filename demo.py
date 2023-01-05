print("hello")
a = 30
b = 40
if b < a:
    print("fdv")
else:
    print("a is not greater than b")
# list datatype
values = [1, 2, 3, 4, "Neha", 6.7]
print(values[4])  # print single value
values.insert(5, 'Rana')  # add new values in b/w the indexes
print(values)
print(values[-1])  # to get last value from the index
values.remove('Rana')  # removing value from the index
print(values)
values.append("End")  # adding a new value in the end of the list
print(values)
values[2] = "NEHA"  # updating a value
print(values)
del values[2]  # for deleting the index
print(values)

# tuple
val = (1, 2, "Neha", "Rana")
print(val[1])
print(val)

# dictionary
valdic = {41: "neha rana", "neha": 26, "surname": "rana"}
print(valdic[41])
print(valdic["surname"])
#dynamic dictionary
dictionary= {}
dictionary["firstname"] = "Neha"
dictionary["lastname"] = "Rana"
dictionary["Age"] = 26
dictionary["Gender"] = "Female"
print(dictionary)
print(dictionary["lastname"])
