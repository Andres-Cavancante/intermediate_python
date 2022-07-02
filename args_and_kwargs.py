#The key *args allows passage of multiple argumentos to a function. *It's not necessary to write the keyword 'args', only write the '*' in the begginning of an argument name

print('*********','Using args','*********')

def testArgs(norm, *a):
    print('First argument', norm)
    for arg in a:
        print('Sequential arguments', arg)

testArgs('apple', 'banana', 'orange', 'cherry', 'tomato')

print('******************************')

def sumNumbers(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print('The result is', sum)

sumNumbers(5,7,3,7,15)

print('******************************')

#The key *kwargs is the same os *args but used to pass keyworded arguments (key=value)

def testkwargs(**kwargs):
    for n, m in kwargs.items(): #its important to call for the items() method to iterate through the kwargs
        print(f'{n} equals {m}') #n and m being key and value

testkwargs(name='Andrew', age=23, gender='m')

print('******************************')

#Args and kwargs podem ser usados também como argumentos:

def testArgs(norm, norm2, norm3):
    print('First argument', norm)
    print('Second argument', norm2)
    print('Third argument', norm3)

values = ('apple', 'banana', 'orange')
kwargvaues = {"norm": "apple", "norm2": 'banana', "norm3": 'orange'} #this had to be passed as a dictionary. The key values have to the be equal to the function argument names

testArgs(*values) #Here, three arguments are passed as one
print('and')
testArgs(**kwargvaues)

print('******************************')