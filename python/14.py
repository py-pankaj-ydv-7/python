# Fuctions in python 

# def my_function(fName,lName):
#     print(fName+" " +lName)


# my_function("  pankaj","yadav")
# my_function("  shubham","yadav")
# my_function("  sujeet","yadav")
# my_function("  dheeraj","yadav")


# def my_function(*fName): # *(astrik lagane se ye tuple me convert kar deta hai )
#     print(fName)


# my_function("  pankaj","yadav")
# my_function("  shubham","yadav")
# my_function("  sujeet","yadav")
# my_function("  dheeraj","yadav")


# def my_function(fruits):
#     for x in fruits:      # ye disct me hai sayad
#         print(x)

# fruit = ["apple","banana","orange"]
# my_function(fruit)



# def my_function(num):
#     return num * 2

# val = my_function(10)
# print(val) 


#  list me ese print karate hai 


def my_function(n):
    result = []
    for x in n:
       result.append(x*2)
    return result

num = [1,2,3,4,5]

val = my_function(num)  
print(val) 