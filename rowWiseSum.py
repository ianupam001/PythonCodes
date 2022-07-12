# def rowWiseSum(li):
#     nrows=len(li)
#     mCols=len(li[0])

#     for i in range(nrows):
#         sum=0
#         for j in range(mCols):
#             sum+=li[i][j]
#         print(sum,end=' ')

# li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# rowWiseSum(li)
# li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# for j in range(4):
#     for ele in li:
#         print(ele[j],end = " ")
def fun(n):
    if n==0:
        return
    print(n%2)
    fun(n//2)
n=25
print(fun(n))