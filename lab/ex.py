def isprime(n):
	"""Test an integer, if it's a prime, return true.
        >>> isprime(19)
        True
        """
	i=2
	assert n>=2,"n must be equal or greater than two"
	flag=True
	while(i<n):
		if n%i==0:
		   flag=False
		i+=1
	return flag


def choose(n, k):
    """Returns the number of ways to choose K items from
    N  items.
    >>> choose(5, 2)
    10
    >>> choose(20, 6)
    38760
    """
    nom,denom=1,1
    nomto=n-k+1
    while(n>=nomto):
    	nom*=n
    	n-=1
    while (k>0):
        denom*=k
        k-=1
    return nom//denom     

def square(x):
    return x * x
def square_every_number(n):
    """Prints out the square of every integer from 1 to n.
    >>> square_every_number(3)
    1
    4
    9
    """
    i=1
    while(i<=n):
        print (square(i))
        i+=1
def double(x):
    return 2 * x
def double_every_number(n):
    """Prints out the double of every integer from 1 to n.
    >>> double_every_number(3)
    2
    4
    6
    """
    i=1
    while(i<=n):
    	print (double(i))
    	i+=1


def every(func, n):
	"""
	>>> def square(x):
	...    return x*x
	>>> every(square,3)
	1
	4
	9
    """

	def sum(n):
		i=1
		while (i<=n):
			print (func(i))
			i+=1
	return sum(n)


def keep(cond, n):
    """Prints out all integers from 1 to n that return True
    when called with cond.
    >>> def is_even(x):
    ...     return x%2 == 0
    >>> keep(is_even, 5)
    2
    4
    """
    i=1
    while (i<=n):
    	if cond(i):
    		print (i)
    	i+=1


def and_add(f, n):
    """Returns a new function. This new function takes an argument
    x and returns f(x) + n.
    >>> def square(x):
    ...     return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    
    def ret(x):
    	return f(x)+n
    return ret

def countdown(n):
   

    if n<1:
       return
    else:
        countdown(n-1)
    print(n)

def expt(base, power):
    if power==0:
        return 1
    elif power>0:
        return expt(base,power-1)*base
    else:
        return expt(base,power+1)/base


def is_prime(n):
    def even_divide(i):
        if i>=n:
            return True
        else:
            if n%i==0:
                return False
        return even_divide(i+1)
    return even_divide(2)



def sum_primes_up_to(n):
    if n==2:
        return 2
    else:
        if is_prime(n):
            return n+sum_primes_up_to(n-1)
        else:
            return sum_primes_up_to(n-1)


def count_stair_ways(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)



def pascal(row, column):
    if column>row:
        return 0
    elif column==0 or column==row:
        return 1
    else:
        return pascal(row-1,column)+pascal(row-1,column-1)


def has_sum(sum, n1, n2):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 1(5) + 0(3) = 5
    True
    >>> has_sum(11, 3, 5) # 2(3) + 1(5) = 11
    True
    """
    if sum<n1 and sum<n2:
        return False
    elif sum==n1 or sum==n2:
        return True
    else:
        return (has_sum(sum-n1,n1,n2) or has_sum(sum-n2,n1,n2))



def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer A prints within this range;
    ... # the TAs would be satisfied with any number it prints
    ...
    True
    >>> sum_range(40, 55) # Printer A can print some number 56-60
    ... # copies, which is not within the TA acceptable range
    ...
    False
    >>> sum_range(170, 201) # Printer A + Printer B will print
    ... # somewhere between 180 and 200 copies total
    ...
    True
    """
    def sum_page(sum_low,sum_high):
        if lower<=sum_low and upper>=sum_high:
            return True
        elif sum_low>=lower and sum_high>upper:
            return False
        else:
            return sum_page(sum_low+50,sum_high+60) or sum_page(sum_low+130,sum_high+140)
    return sum_page(0,0)




