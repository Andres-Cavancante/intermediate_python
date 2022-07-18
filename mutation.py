#There are mutable and immutable datatypes in python
#Mutability: whenever a variable is assigned to another variable of mutable datatype, any changes to the data are reflected by both variables

print('*********','Mutability','*********')

foo = ['hi']
print(foo) #Output: ['hi']

bar = foo
bar += ['bye']
print(foo) #Output: ['hi', 'bye']
print(bar) #Output: ['hi', 'bye']

#The foo variable is not changed but since it is a mutable datatype, any change made to the bar variable since attribution is also made to foo

print('******************************')

#In Python the default arguments are evaluated once when the function is defined
#An example of how a mutable datatype should be passed as an argument:

# def add_to(element, target=None):
# if target is None:
# target = []
# target.append(element)
# return target

#List of data types mutability

# List - Mutable
# Set - Mutable
# Dict - Mutable
# Bool - Immutable
# Int - Immutable
# Float - Immutable
# Tuple - Immutable
# Str - Immutable
# Frozenset - Immutable