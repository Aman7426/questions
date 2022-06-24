"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n"""

def sumsquare():
    ''' Returns sum of square of all positive numbers less than n '''
    sqrsum = 0
    try:
        inpdata = int(input("Enter a number > "))
        if inpdata <= 2:
            print ("Sum of square is 1")
        else:
            for k in range(inpdata):
                sqrsum += k**2
            print("\n\nSum of square of element < %d is %d " % (inpdata,sqrsum))
    except Exception as excpt:
        print ("Yikees! ", excpt)
    return



sumsquare()

