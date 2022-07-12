# n = int(input())
# for i in range(1, n+1, 1):
#     for s in range(n-i):
#         print(" ", end='')
#     for j in range(i, 2*i, 1):
#         print(j, end='')
#     for j in range(2*i-2, i-1, -1):
#         print(j, end='')
#     print()
i=1
while i<3:
    j=0
    while j<5:
        j = j +1
        if j==3:
            continue
        print(j,end=" ")
    i = i +1
