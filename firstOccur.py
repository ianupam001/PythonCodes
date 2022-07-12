# slicing method
def firstOccur(arr,n):
    length=len(arr)
    if length==0:
        return -1
    if arr[0]==n:
        return 0
    if (firstOccur(arr[1:],n)==-1):
        return -1
    else:
        return (firstOccur(arr[1:],n)+1)
# better approach
def firstIndexBetter(arr,n,si=0):
    length=len(arr)
    if si==length:
        return -1
    if arr[si]==n:
        return si
    return firstIndexBetter(arr,n,si+1)
num=5
li=[1,2,3,1,5,7,5]
print(firstOccur(li,num))
print(firstIndexBetter(li,num))


