# Q9
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def fun(x,y):
        if x==m-1 or y==n-1:
            return 1
        else:
            return fun(x+1,y)+fun(x,y+1)
    return fun(0,0)

# Q10
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a%b==0:
        return b
    elif b%a==0:
        return a
    else:
        if a>=b:
            return gcd(a%b,b)
        else:
            return gcd(a,b%a)