"""
print given pattern:
n=4
1
12
123
1234
"""
n=int(input("Enter a number:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    print()
    i+=1
"""
print pattern given below:
n=5
1
23
345
4567
56789
"""
n=int(input("Enter a number:"))
i=1
while i<=n:
    j=1
    p=i
    while j<=i:
        print(p,end='')
        j+=1
        p+=1
    print()
    i+=1
"""
print pattern given below:
1
23
456
78910
"""
n=int(input("Enter a number:"))
i=1
q=i
while i<=n:
    j=1
    while j<=i:
        print(q,end=' ')
        q+=1
        j+=1
    print()
    i+=1
    