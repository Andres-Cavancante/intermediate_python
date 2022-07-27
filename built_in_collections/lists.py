print('*********','Lists','*********', '\n', sep='')
#Lists are used to store multiple values in a single variable
#Creating a list:
some_list = ['banana', 5, 6, 6, 'pêssego', True] #List accept duplicates and can be of any datatype
print(some_list) #output: ['banana', 5, 6, 'pêssego', True]

#The list() function returns a list
some_other_list = list()
print(some_other_list) #output: []
fruit = 'banana'
some_other_list = list(fruit)
print(some_other_list) #output: ['b', 'a', 'n', 'a', 'n', 'a']

print('\n', '*********','Accessing elements','*********', '\n', sep='')

#Retrieving elements by index:
print(some_list[0]) #output: banana
print(some_list[0][3]) #output: a

#Iterating over the list elements
for x in some_list:  
    print(x, end="-") #output: banana-5-6-6-pêssego-True-6

#Getting the length of the list:
print('\n','The length is: ', len(some_list), sep='') #output: The length is: 6

#Element evaluation:
if 'pêssego' in some_list: #If there's a 'pêssego' in the list, it'll evaluate True
    print('okay') #output: okay

print('\n', '*********','Adding Items','*********', '\n', sep='')

#Element adition:
#The append() function inserts elements at the end of the list
third_list = list()
third_list.append('first_element')
third_list.append('second_element')
print(third_list) #output: ['first_element', 'second_element']

#The insert(positino, value) function allow addiction of a value in a specific position 
third_list. insert(1, 'element_x')
print(third_list) #output: ['first_element', 'element_x', 'second_element']

print('\n', '*********','Removing Items','*********', '\n', sep='')

#Removing itens:

#The pop(index) function returns the element at the index specified and removes the same element from the list. The index argument is
#optional, with the default value of -1 (last element)
list_pop = ['banana', 5, 6, 'pêssego', True]
print(list_pop)
pop_value = list_pop.pop(1)
print('Value removed:', pop_value,'new list:', list_pop)

#The remove() function removes the first matching value in the list specified as an argument
list_remove = ['banana', 5, 6, 'pêssego', True]
print(list_remove)
list_remove.remove('pêssego')
print(list_remove)

#The clear() method removes all items from a list
list_remove.clear()
print('Function cleared:', list_remove)

print('\n', '*********','Other functions','*********', '\n', sep='')

#The list datatype has some more features:

#The reverse() method mirrors the elements positions:
list_reverse = ['banana', 5, 6, 'pêssego', True]
print('Normal list:', list_reverse, ', reversed list:', end=' ')
list_reverse.reverse() #This method changes the list but returns None
print(list_reverse)

#The sort(reverse, key) method sorts the function in ascending order by default or by any criteria specified as a key
#To not mutate the list, use sorted(list)
list_sort = [-5, 10, 300, -35, 23]
list_sort.sort(reverse=True)
print(list_sort)

print('\n', '*********','Operations','*********', '\n', sep='')

#A list state can be multiplied by a particular value
fourth_list = [5, 6] * 5
print(fourth_list)

fifth_list = ['something']

#Lists can be concatenated:
print(fourth_list + fifth_list * 3)

#Slicing is a very common operation: list[start:end:step]
sixth_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(sixth_list[0:10:2])

#Lists are mutable, so to avoid changing them directly, the copy() function is used as in: list_copy = any_list.copy()
#Another way is getting the elements by slicing: list_copy = any_list[:]

#Lists can take iterable statements in their declaration:
a = [1,2,3,7,17,19,37]
b = [i*i*i for i in a]
print(b)