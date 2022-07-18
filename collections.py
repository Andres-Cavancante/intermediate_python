from collections import Counter, namedtuple, OrderedDict, deque

print('*********','Recaptulating dicts','*********')
#dictionaries are used to store data values in key:value pairs
person = {"name": "Bob", "age": 29, "height": "178cm"}
print(person)
print(person["name"])
print(type(person))

print('*********','Using defaultdict','*********')
from collections import defaultdict
#a dict that can store a default value type in case the accessed key doesn't have a value
dict_default = defaultdict(int) #the standard value will be 0 (int)
dict_default['name'] = 'Andrew'
print(dict_default['name'], dict_default['city'])

