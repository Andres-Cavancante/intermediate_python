print('*********','Using sets','*********')

#Sets are data structures pretty similar to lists but cannot contain duplicate values
#The set function transforms variables in sets 
set_string = set('comunication')
print(set_string)
#var = {} is a dict

print('******************************')

#Sets are an elegant solution to check duplicates in a list:
#Sintax: set([function])

letters = ['e','b','n','g','e','f','f','t','a','b']
duplicates = set([x for x in letters if letters.count(x) > 1])
print(duplicates)

print('******************************')

#add and remove
odd = set([1,3,5,7,9,50])
even = set([2,4,6,8,10])
odd.add(11)
odd.remove(50)
print(odd)
#se a função remove() receber um elemento que não está contido no set, ERRO. A função discard funciona da mesma forma mas caso receba um elemento não contido no set, não faz nenhuma alteração

print('******************************')

#Sets (Math):
prime = {2,3,5,7,11} #sets can also be defined with this sintax
#union:
union = odd.union(even)
print(union)
#intersection:
intersection = even.intersection(prime)
print(intersection)
#difference (contained in the first set but not the second):
difference = even.difference(prime)
print(difference)
#symetric difference (all values except the common)
simetricDifference = odd.symmetric_difference(prime)
print(simetricDifference)

print('******************************')

#verify subset condition
subsetOfOdd = {3,5}
print(odd.issubset(even))
print(subsetOfOdd.issubset(odd))
#verify superset condition
# print(.issuperset())
# print(.issuperset())

#verify disjoint (if the join between sets is null)
# print(.isdisjoint())

print('******************************')

# update
print('update: ')
print(odd)
print(even)
odd.update(even)
print(odd)
#there's also intersection_update, difference_update(), symmetric_difference_update()

print('******************************')

#Clear set:
prime.clear()
print(prime)

print('******************************')

#pop() function removes a random item
print(odd)
print(odd.pop())
print(odd)

print('******************************')

#Modify a set's copy also modifies the original. copy() and set() methods can be used to copy

#frozenset its an imutable set:
a = frozenset([1,5,67,8,4])
print(a)
#a.pop()
#print(a)