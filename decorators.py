print('*********','Function Principles','*********')

def f1():
    print('calling f1')

print(f1) #output: <function f1 at 0x00000198E80A31C0>
#this shows f1 is an object, so a function can be manipulated just like any other object

print('******************************')

#passing a function as an argument:
def f2(f):
    f()
f2(f1) #output: calling f1

print('******************************')

#passing a function as an argument and returning another function

def f3(func):
    def wrapper():
        print('Started')
        func()
        print('Ended')
    return wrapper

f3(f1) #this calling doesn't return anything, since the wrapper function itself is never calleed

f3(f1)() #using this sintax, the function wrapper can be called

print('*********','Using Decorators','*********')

def f():
    print('Middle')

f = f3(f) #this sintax assigns the f3 function with f as an argument to the object f
f()

print('******************************')

@f3 #this is equivalent to f = f3(f)
def f():
    print('Mid') #a decorator is symbolized by the @

f()
# f('Hi') - this will raise an exception since the wrapper function doesn't accept any argument
# to make sure the calling can have arguments

print('******************************')

def f3(func):
    def wrapper(*args, **kwargs):
        print('Started')
        func(*args, **kwargs)
        print('Ended')
    return wrapper

@f3
def f(a):
    print(a)

f("Middle") #parei na página 24