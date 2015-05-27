# CS 61A Fall 2014
# Name:
# Login:


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    "*** YOUR CODE HERE ***"
    return (a==b and b!=c) or (a==c and b!=c) or (b==c and a!=b)


def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    i,j=a,b
    flag=False
    if a==1 or b==1:
        flag=True
    while (i!=1):
        if i==b:
            flag=True
        if i%2==1:
            i=i*3+1
        else:
            i=i/2
    while (j!=1):
        if  j==a:
            flag=True
        if  j%2==1:
            j=j*3+1
        else:
            j=j/2
    return flag
        


def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    "*** YOUR CODE HERE ***"
    width,height=perimeter//2-1,1
    difference=perimeter
    wi,he=width,height
    while (width>=1):
        if (abs(width/height-1-height/width)<difference):
            wi,he,difference=width,height,abs(width/height-1-height/width)
        height+=1
        width-=1
    return min(wi,he)


