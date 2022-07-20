#Python has a series of very interesting built-in functions:
#The any() funcion runs through an iterable and returns True if any of its elements is True
print('*********','Function Any','*********')
list_of_booleans = [False, False, False, True]
print(any(list_of_booleans)) #output: True
numbers = [9,4,5,6,1,2,0]
print(any(numbers)) #output: True

print('*********','Function All','*********')
#The all() function runs through an iterable and returns True if all elements evaluate to True
print(all(numbers)) #output: False
numbers.remove(0)
print(all(numbers)) #output: True

print('******************************')
#The functions min(), max() and sum() return the minimum, maximum and the sum of the values respectively in a sequence
print('*********','Functions min(), max() and sum()','*********')
print('numbers:', numbers)
print('min value of numbers:', min(numbers))
print('max value of numbers:', max(numbers))
print('sum of numbers:', sum(numbers))