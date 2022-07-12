def isPrime(n,k=2):
    if n<=2:
        return True if (n==2) else False
    if n%k==0:
        return False
    if k*k>n:
        return True
    return isPrime(n,k+1)
n=int(input())
if isPrime(n):
    print("Yes")
else:
    print("No")
