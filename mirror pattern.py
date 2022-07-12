"""
*        *
**      **
***    ***
****  ****
"""
n = int(input())
i = 1
while i <= n:
    spc = 1
    while spc <= n-i:
        print(" ", end='')
        spc += 1
    star = 1
    while star <= i:
        print("*", end='')
        star += 1
    print()
    i += 1

# Isosceles pattern


n = int(input())
i = 1
while i <= n:
    # spaces
    spc = 1
    while spc <= n-i:
        print(" ", end='')
        spc += 1
    # increasing pattern
    num = 1
    while num <= i:
        print("*", end='')
        num += 1
    # decresing pattern
    p = i-1
    while p >= 1:
        print("*", end='')
        p -= 1
    print()
    i += 1
