# set :  - collection of data ko store karte hai . isme {} use hota hai 


# myset ={"apple","banana","cherry"}
# # print(type(myset))


# # constructor type esaa hota hai


# myset2 = set(("apple","banana","cherry","pankaj","yadav"))
# print(myset2)
# print(len(myset2))

# thisset = isme hum duplicate nahi kr sakte hai . isme allow nahi hote hai
# false pahla aata hai qki ye inorder me hota hai 

# thisset = {1,2,2,3,}
# thisset = {1,2,2,3,True,False}
# print(thisset)

# thisset = {1,2,2,3,True,False}
# print(1 in thisset)

#  add, or remove kr sakte hai 

# thisset = {1,2,3}
# thisset.add(4)
# thisset.remove(1)
# print(thisset)


# thisset1 = {1,2,3}
# thisset2 = {4,5,6}

# thisset1.update(thisset2)

# print(thisset1)


#  do set jud k dusari jagah pe chale jaye ye sab possible hai union se 

# thisset1 = {1,2,3}
# thisset2 = {4,5,6}
# thisset3 = thisset1.union(thisset2)
# print(thisset3)



# intersection se duplicate pata chal jata hai 

thisset1 = {1,2,3}
thisset2 = {4,5,6,3}

# thisset3 = thisset1.intersection_update(thisset2)
# print(thisset1)


# thisset3 = thisset1.intersection(thisset2)
# print(thisset3)