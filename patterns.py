"""
print pattern like give  below
n=4
****
****
****
****
"""
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print('*',end='')
        j+=1
    print()
    i+=1
"""
print pattern like given below:
m=4
1111
2222
3333
4444
"""
m=int(input())
k=1
while k<=m:
    l=1
    while l<=m:
        print(k,end='')
        l+=1
    print()
    k+=1
"""
print the pattern given below:
p=4
1111
2222
3333
4444 
"""
p=int(input())
x=1
while x<=p:
    y=1
    while y<=n:
        print(y,end='')
        y+=1
    print()
    x+=1
"""
print pattern given below:
q=4
4321
4321
4321
4321
"""
q=int(input())
s=q
while s>0:
    t=q
    while t>0:
        print(t,end='')
        t-=1
    print()
    s-=1

