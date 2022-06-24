"""Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators"""

def is_even(k):
    if k%2==0:
        return print("true")
    else:
        print("false")

kk=is_even(4)
jj=is_even(5)