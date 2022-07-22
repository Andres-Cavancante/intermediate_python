#Map is a function that can apply a function to all the items in an input list
#Sintax: map(function_to_apply, list_of_inputs)

print('*********','Using map','*********')

items = [2,4,7,8,9,14]
squared = list(map(lambda x: x*x, items)) #The map function returns a map object, so the list function is used to return a list
print(squared) #Lambda functions are frequently used with map. But it can be any function

print('******************************')

def multiply(x):
    return (x*x)    
def add(x):
    return (x+x)

funcs = [multiply, add] #In this case, a list of functions in being passed as the list of inputs
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

print('******************************')

#The filter function returns a list of elements for which a function returns true
#Sintax: filter(function_to_filter, list_of_inputs)

numbers = range(-10,10)
negative = list(filter(lambda x : x < 0, numbers))
print(negative)

print('******************************')