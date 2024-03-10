# Disctionaries :-  isme kya hota hai ki , key or value ka pair hota hai .

thisdict = {
    "fname": "pankaj",
    "lname": "yadav",
    "age":20
}

# print(thisdict.get("age"))
thisdict["age"] = 22
thisdict["greeting"] = "Hello"
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())
# print(type(thisdict.items()))

# print(thisdict)
# print(thisdict["fname"])


# print(len(thisdict))

# constructor k form me ese likhte hai 

# thisdict2 =  dict(
#     fname =  "pankaj",
#     lname =  "yadav",
#     age = 20
# )

# print(thisdict2)


# nested disct

myfamily = {
    "child1" : {
        "name": "py",
        "year": 2004
    },
    "child2" : {
        "name" : "py3",
        "year" : "2005"
    }
}

print(myfamily)
print(myfamily["child1"])
print(myfamily["child2"])
print(myfamily["child2"]["name"])