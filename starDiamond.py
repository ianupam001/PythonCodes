n = int(input())
n1 = (n+1)//2
n2 = n//2
i = 1
while i <= n1:
    spc = 1
    while spc <= (n1-i):
        print(" ", end='')
        spc += 1
    star = 1
    while star <= (2*i)-1:
        print("*", end='')
        star += 1
    print()
    i += 1
i = n2
while i >= 1:
    spaces = 1
    while spaces <= (n2-i+1):
        print(" ", end='')
        spaces += 1
    j = 1
    while j <= (2*i)-1:
        print("*", end='')
        j += 1
    print()
    i -= 1
