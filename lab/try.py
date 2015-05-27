Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def isprime(n):
	i=2
	assert n>=2,"n must be equal or greater than two"
	flag=True
	while(i<n):
		if n%i==0:
		   flag=False
		i++
	return flag

SyntaxError: invalid syntax
>>> def isprime(n):
	i=2
	assert n>=2,"n must be equal or greater than two"
	flag=True
	while(i<n):
		if n%i==0:
		   flag=False
		i+=1
	return flag

>>> isprime(2)
True
>>> isprime(19)
True
>>> isprime(1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    isprime(1)
  File "<pyshell#2>", line 3, in isprime
    assert n>=2,"n must be equal or greater than two"
AssertionError: n must be equal or greater than two
>>> def isprime(n):
	"""Test an integer, if it's a prime, return true.
        >>>isprime(19)
        False
        """
	i=2
	assert n>=2,"n must be equal or greater than two"
	flag=True
	while(i<n):
		if n%i==0:
		   flag=False
		i+=1
	return flag
