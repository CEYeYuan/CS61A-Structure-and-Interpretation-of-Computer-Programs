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