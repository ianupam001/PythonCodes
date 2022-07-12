# finding nCr
def factorial(n):
    fact = 1
    for i in range(1, n+1, 1):
        fact *= i
    return fact


def nCr(n, r):
    c = factorial(n)//(factorial(r)*factorial(n-r))
    return c


n = int(input("Enter n:"))
r = int(input("Enter r:"))
print(nCr(n, r), end='')
