# print multiples of 3

# inefficient method
# a = int(input())
# b = int(input())
# for i in range(a, b+1, 1):
#     if i % 3 == 0:
#         print(i)

# efficient method print multiples of 3
x=int(input())
y=int(input())

if x%3==0:
    s=x
elif x%3==1:
    s=x+2
else:
    s=x+1
for i in range(s,y+1,1):
    print(i,end=' ')

# checking prime number
n=int(input())
flag=True
for i in range(2,n,1):
    if n%1==0:
        flag=False
if flag:
    print("not prime")
else:
    print("prime") 