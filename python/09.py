# Tuple

# tuple k pass item unchangeble hote hai , duplicate item ye bhi rakhte hai 

mytuple =("apple", "banana", "cherry", "apple")
# print(len(mytuple))
# mytuple[0] = "hemlo" # does not support item assignment , because tuple is unchangeble

myList = list(mytuple)

myList = list((mytuple))
myList.append("orange")
# print(mytuple)
# print(myList)


myNewTuple = tuple(("hello","hii"))

myNewTuple = tuple(myList)
# print(mytuple)
# print(myList)
# print(len(myNewTuple))

# print(type(mytuple))
# print(type(myNewTuple))
# print(type(myList))


# mytuple = ("apple", "banana", "cherry", "apple")

# if "apple" in mytuple:
#     print("Yes it is there in the Tuple")

# myList = list(mytuple)
# myList[1] = "orange"
# myList.append("orange")
# mytuple = tuple(myList)
#  remove karne k liye list banake remove kr sakte hai 

# y= ("orange",)
# mytuple += y
# print(mytuple)

# print(mytuple,myList)


mytuple = ("apple", "banana", "cherry")

(a,b,c) = mytuple  # or agar kahi abc me se koi variable na le ya fir koi variable jada le le to error deta hai thik hai beta

print(a)
print(b)
print(c)


# mytuple = ("apple", "banana", "cherry","Hello","World")

# (a,b,c,*d) = mytuple  

# print(a)
# print(b)
# print(c)
# print(type(d))  # yaha kya hua ki astrik lagane se d me sari bachi hui value a gayi hai .....



mytuple = ("apple", "banana", "cherry","Hello","World")

multiTuple = mytuple *5

print(multiTuple)