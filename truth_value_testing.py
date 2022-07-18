#The Python constants that evaluate to False are None and False
#The bool() function evaluates the boolean value of the argument
#In Python, the common 'Null' in other languages is None
print('************','Evaluating False and None','************')
is_true = False
is_true_too = None

print(bool(is_true)) #output: False
print(bool(is_true_too)) #output: False

#Numeric values zeroed evaluate to false
print('************','Evaluating Numeric values','************')
number_one = 0
number_two = 0.0
number_three = 0j #Complex values
if not number_one and not number_two and not number_three:
    print('All False') #output: All False
#Decimal(0) and Fraction(0,x) objects zeroed also evaluate to False

#Empty sequences evaluate to false
print('************','Evaluating Empty Collections','************')
collection_one = '' #empty string
collection_two = {} #empty dict
collection_three = [] #empty list
collection_four = () #empty tuple
if not collection_one and not collection_two and not collection_three and not collection_four:
    print('All False') #output: All False

#Empty sets and range evaluate to false
print('************','Evaluating Empty sets and Empty ranges','************')
empty_set = set()
range_zero = range(0)
if not empty_set and not range_zero:
    print('Both False') #output: All False