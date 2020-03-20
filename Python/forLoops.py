# Iterable - go over an object especially item by item: A string is iterable - can go over character by character
# eg: "Hello" we can go over 'H' 'e' 'l' 'l' 'o'
# eg: List of numbers [1,2,3,4] we can go over [1] [2] [3] [4] or 1 2 3 4
# Dictionary is iterable

myList = [1,2,3,4,5]
for item in myList: #the variable name after 'for' can be anything
    print (item)
print("\n")

#print every character in the string "Hello"
for _ in 'Hello':
    print(_)
print("\n")

#print last tuple item in list (tuple unpacking)
tupleList = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in tupleList:
    print (c)
print("\n")

myDictionary = {'key1':1, 'key2':2, 'key3':3}
for item in myDictionary:
    print(item)
print("\n")
myDictionary = {'key1':1, 'key2':2, 'key3':3}
for key,value in myDictionary.items():
    print(value)