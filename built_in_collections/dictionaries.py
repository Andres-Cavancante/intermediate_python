#dictionaries are collections of mutable unordered key-value pairs

print('*********','Dictionaries','*********')
dict_1 = {"name": "Mario", "city": "Curitiba", "age": 34}
print(dict_1)
print(dict_1.items()) #returns the key-value pairs
print(dict_1.keys()) #returns only the keys

print('*********','Dict() Function','*********')
#The dict() function receives key=values as parameters and returns a dictionary
var_dict = dict(name="Jorge", city="Nova Orleans", age=23)
print(var_dict)

print('*********','Accessing values','*********')
#accessing values:
print(var_dict["city"])
#adding values:
var_dict["email"] = "jorge@gmail.com"
print(var_dict)
#excluding values:
del var_dict["email"] 
print(var_dict)
#var_dict.pop("key") - remove a specified key
#var_dict.popitem() - removes the last key

print('*********','Conditionals','*********')
#conditionals:
if "city" in var_dict:
    print(var_dict["city"])

for x in var_dict:
    print(x)

for x in var_dict.values():
    print(x)

for x, y in var_dict.items():
    print(x,y)

#dictionary is a mutable datatype - the copy() function must be used to create an unrelated copy

print('*********','Update Function','*********')
#the update() function updates a dictionary with data from other dictionary if they have the same keys. The particular keys are agglutinated
dict_1 = {"name": "Mario", "city": "Curitiba", "age": 34, "mother": "Cecilia"} 
var_dict = dict(name="Jorge", cpf=123457544567, city="New Orleans", age=23)
dict_1.update(var_dict)
print(dict_1)