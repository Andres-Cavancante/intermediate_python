#Python has a series of very interesting built-in functions:
#The iter() function creates an iterator over a collection
print('*********','Function iter()','*********')

days = ["Sunday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daysPT = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

i = iter(days) #the iterator defined is the i variable
print(next(i)) #The next() function will return the object in the index i of the collection and increment i
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i),"\n")
#print(next(i)) #When the iterator exceeds the length of the collection, an exception will be raised

print('*********','Function iter() with sentinel','*********')
with open('C:\\Users\\burge\\OneDrive\\Documentos\\Projetcs\\intermediate_python\\util\\lines_list.txt', 'r') as t:
    for line in iter(t.readline, ''): #the readline method returns one line from the file #the second parameter for iter() is a sentinel, used to represent the end of a sequence. Its only logical in a loop. *when the sentinel is used, the first term must be a callable
        print(line.strip()) #the strip() function removes spaces and new lines in the string line

print('*********','Function enumerate()','*********')
#The enumerate() function returns the object in the collection along with its index

for count, day in enumerate(days):
    print(count, day)

print('******************************')
#the index start can be specified with the start argument

for count, day in enumerate(days, start=7):
    print(count, day)

print('*********','Function zip()','*********')
#the zip can be used to combine collections in tuples

for value in zip(days, daysPT):
    print(value) #for each 'value', a tuple with both objects is returned
    print(value[0], 'is', value[1]) #or

print('*********','Combining enumerate() and zip()','*********')
#interesting results can be created from combining enumarate and zip

for en, pt in enumerate(zip(days, daysPT), start=1):
    print(en, pt[0], '=', pt[1]) #the loop is exhausted as soon as the shortest collection is expired