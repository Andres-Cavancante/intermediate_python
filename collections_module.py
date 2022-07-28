#The collections module implements container datatypes providing alternatives to Python's general purpose built-in containers

print('*********','Using defaultdict','*********')
from collections import defaultdict #its good practice to import all needed libraries at the beggining of the file.
#defaultdict is a regular dictionary that can store a default value type in case the accessed key doesn't have a value
#This is useful when it's necessary to modify a key in the dictionary that hasn't already been inserted
dict_default = defaultdict(int) #the standard value will be 0 (int)
dict_default['name'] = 'Andrew'
print(dict_default['name'], dict_default['city']) #The .get calling will return None
another_dict = defaultdict(list) #the standard value will be an empty list
print(another_dict['something'])
#defaultdict receives a default_factory, which is a function specifying a value
final_dict = defaultdict(lambda: 100)
print(final_dict['something'])


print('*********','Using namedtuples','*********')
from collections import namedtuple
# Named tuples assign meaning to each position in a tuple and allow for more readable, 
# self-documenting code. They can be used wherever regular tuples are used. But tuple elements can only be
# accessed by position index while in namedtuples they add the ability to access fields by name.

Point = namedtuple('Point', 'x,y,z')
P1 = Point(0, 4, -1)
P2 = Point(2, 2, 5)
print(P1, P2)
print(P1.z, P2.x, P1.y)

print('*********','Using Counters','*********')
from collections import Counter
#The counter is a dict subclass for counting hashable objects

breaking_bad = ["Walter", "Jesse", "Skyler", "Walter", "Hank", "Saul", "Marie"]
stranger_things = ["Eleven", "Mike", "Lucas", "Will", "Max", "Dustin", "Steve"]

c1 = Counter(breaking_bad) #initializing counter as c1
c2 = Counter(stranger_things)

print(c1["Walter"]) #This will return how many time the value "Walter" appears in the breaking_bad list
print(c1.values()) #The values method returns the frequency of occurrence for each diferent value 
print(sum(c1.values())) #The frequencies can be summed. This will return the number of elements

c1.update(c2) #The update() method will combine the two classes in the counter
print(c1.values())
print(sum(c1.values()))

print(c1.most_common(3)) #The most common method(n) will return the n most common values from the counter. If no argument is passed, it will list all values

c1.subtract(c2) #The subtract mehtod will separate the values of c2 from c1 again
print(c1.values())

print(c1 & c2) #With the and operator, the intersection can be retrieved (none in this case)

print('*********','Using ordereddict','*********')
from collections import OrderedDict
# OrderedDict is a regular dictionary that can store information about the insertion order of the key-value pairs. 
# Since Python 3.7, the dict class has this hability by default
# For two ordered dicts to evaluate the same, they must have the same items in the same order

ord_dict = OrderedDict()
ord_dict['a'] = 1
ord_dict['c'] = 4
ord_dict['b'] = 3
ord_dict['d'] = 2
print(ord_dict)

print('*********','Using deque','*********')
from collections import deque
# Deque is preferred over a list in the cases where quicker append and pop operations are needed from both the ends of the container

deque_ = deque() # Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.
deque_.append(1)
deque_.append(2)
deque_.append(3)
print(deque_)
deque_.appendleft(4) # The pop(), extend(), etc. functions also can be used fun the left 
print(deque_)

deque_.rotate(3) #The rotate() method deslocates all elements n times to the right. If it receives a negative n, to the lefts
print(deque_)