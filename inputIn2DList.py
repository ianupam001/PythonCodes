'''
# input in 2D list  using list comprehension
str=input().split()
n,m=int(str[0]),int(str[1])
li=[[int(j) for j in input().split()] for i in range(n)]
print(li)

# input in jagged list
n=int(input())
li1=[[int(j) for j in input().split()] for i in range(n)]
print(li1)'''
# input in 2-D list in one line
str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
li=[[int(b[m*i+j]) for j in range(m)] for i in range(n)]
print(li)

# taking n,m and total input in one line 3 4 1 2 3 4 5 7 8 9 10 11 12
str=input().split()
n,m=int(str[0]),int(str[1])
b=str[2:]
li2=[[int(b[m*i+j]) for j in range(m)] for i in range(n)]
print(li2)