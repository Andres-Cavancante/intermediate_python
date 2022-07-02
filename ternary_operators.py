#Ternary operators are more commonly known as conditional expressions in python
#They are basically a simplification of the if else logic
#Sintax: condition_being_true if condition else condition_being_false

print('*********','Using ternary operators','*********')

def checkEven(*args):
    result = []
    for arg in args:
        result.append(str(arg) + ' is even' if arg%2==0 else str(arg) + ' is odd')
    print(result)

checkEven(1,2,3,4,5,6,7,8,9,10)