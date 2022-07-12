# Printing kth alphabet
k = int(input("Enter a number(1-26):"))
x = ord('A')
asciiTarget = x+k-1
asciiChar = chr(asciiTarget)
print(asciiChar)
"""
printing character pattern:
n=4
ABCD
ABCD
ABCD
ABCD
"""
n = int(input("Enter a number:"))
i = 1
while i <= n:
    j = 1
    while j <= n:
        charP = chr(ord('A')+j-1)
        print(charP, end='')
        j += 1
    print()
    i += 1
"""
print pattern as given below
n=4
ABCD
BCDE
CDEF
DEFG
"""
n = int(input("Enter a number:"))
i = 1
while i <= n:
    start_char = chr(ord('A')+i-1)
    j = 1
    while j <= n:
        charP = chr(ord(start_char)+j-1)
        print(charP, end='')
        j += 1
    print()
    i += 1
