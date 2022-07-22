#Docstrings (documentation strings) can be added inside ''' '''
def rand_func(*args):
    '''rand_func(args) --> extends and returns a list with the args as its elements
    '''
    list = []
    for arg in args:
        list.extend(arg)
    return(list)


print(rand_func([2,5,6], ['hoje'], [2])) #output: [2, 5, 6, 'hoje', 2]

#To invoke the documentation:
print(rand_func.__doc__) #output: rand_func(args) --> extends and returns a list with the args as its elements