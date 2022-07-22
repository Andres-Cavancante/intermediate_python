#In Python, it is possible to pass arguments in keyword format:
print('*********','Using keyword argument','*********')
def sum(num1, num2):
    return num1 + num2

print(sum(2,num2=5)) #output: 7

print('*********','Using keyword-only arguments','*********')
#It is possible to force the user to fill an argument with a keywork
def multiply(num1, *, num2):
    return num1 * num2

print(multiply(6,num2=4)) #output: 24