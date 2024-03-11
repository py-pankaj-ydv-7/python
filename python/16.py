# Higher order function:- 

#  map 

def square(x):
    return x**2

numbers = [1,2,3,4,5]
# squared_numbers = list(map(square,numbers))
# squared_numbers = list(map(lambda x : x*x,numbers))   # yaha lamda function ka use kiya map me
# print(squared_numbers)


even_numbers = list(filter(lambda x : x%2 == 0,numbers))
print(even_numbers)