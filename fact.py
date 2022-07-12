# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# n= int(input("Enter a  number:"))
# print(fact(n))
x = int(input("Enter the number of testcases:"))
while(x > 0):
    m = int(input("Enter a number:"))
    fact = 1
    for i in range(1, m+1):
        fact = fact*i
    print("Factorial is:", fact)
    x -= 1
