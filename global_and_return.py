print('*********','Using return','*********')

#the return keyword assigns a value to the variable calling the function

def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print('The result is', add(3,5,6,2))

print('*********','Using global','*********')

#the global keywork allows a variable to be used outside the scope where it's declared

def multiply(*args):
    global res #res can be used anywhere
    res = 1
    for arg in args:
        res *= arg

multiply(2,5,67)
print(res)

#in practical programming it is best to avoid the global keyword as it only makes things difficult by introducing unwanted variables to the global scope

print('*********','Returning two variables','*********')

#when one is trying to return more than one variable from a function, they should not use the global keyword. Some good options are returning the variables as a tuple, list or dict, as in:

def profile():
    name = 'Amelie'
    age = '35'
    return (name, age)

print(profile()[1]) #output: 35

print('******************************')

#or by more common convention:

def profile():
    name = 'Amelie'
    age = '35'
    return name, age

print(profile()[0]) #output: 35