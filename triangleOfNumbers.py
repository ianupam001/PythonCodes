n=int(input())
i=1
while i<=n:
    # spaces
    spc=1
    while spc<=n-i:
        print(" ",end='')
        spc+=1
    # increasing number
    j=1
    num=i
    while j<=i:
        print(num,end='')
        j+=1
        num+=1
    # decreasing pattern
    p=num-2
    while p>=num:
        print(p,end='')
        p-=1
        j+=1
    print()
    i+=1
