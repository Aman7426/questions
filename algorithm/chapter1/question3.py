"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""



def minmax(data):
    a = b = data[0]
    
    for num in data:
        if num>a:
            a = num
        elif num <b:
            b = num
    return a , b

print(minmax([10,2,30,40]))
