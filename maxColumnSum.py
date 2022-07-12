def maxColumnSum(li):
    n=len(li)
    m=len(li[0])

    maxCol_sum=-1    
    maxCol_Indx=-1

    for j in range(m):
        sum=0
        for i in range(n):
            sum+=li[i][j]
        if sum > maxCol_sum:
            maxCol_sum=sum
            maxCol_Indx=j
    return maxCol_Indx,maxCol_sum
li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(maxColumnSum(li),end=" ")    
