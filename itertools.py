#The itertools package has advanced interation functions
import itertools

print('*********','Cycle() Function','*********')
#The cycle() function creates an iterator over a collection, just like the iter() function but it cycles over the collection
sequence = ['first', 'second', 'third', 'fourth']
cy = itertools.cycle(sequence)
result = []
for _ in range(10): #_ in this case is used as an unused value since there's no natural way to loop n times without a counter in Python and the counter is not used
    result.append(next(cy))
print(result) #output: ['first', 'second', 'third', 'fourth', 'first', 'second', 'third', 'fourth', 'first', 'second']

print('*********','Count() Function','*********')
#The count() function creates a counter that can receive a start and a step
ct = itertools.count(100, 100)
result = []
for _ in range(10):
    result.append(next(ct))
print(result) #output: [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

print('*********','Accumulate() Function','*********')
#The accumulate() function acumulates the values over a collection
acc = itertools.accumulate(result) #The operation used (sum, by default) can be changed
print(list(acc)) #accumulate() creates an object - must be converted to a list

print('*********','Dropwhile() and Takewhile() Functions','*********')
# Dropwhile() and Takewhile() functions work siilar to filter transforms. They will iterate over a collection and return values ultil a certain condition is met that stops them
result.append(10) #[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10]
dw = itertools.dropwhile(lambda x : x < 600, result) #drops the values while the condition evaluates true, then return all subsequent values
tw = itertools.takewhile(lambda x : x < 600, result) #returns the values while the condition evaluates true, then doesn't return anymore values
print(list(dw))
print(list(tw))