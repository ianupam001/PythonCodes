# iterative version
def firstOccurence(arr,n,x):
    low=0
    high=n-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            if mid==0 or arr[mid-1] != arr[mid] :
                return mid
            else:
                high=mid-1
    return -1
# recursive version
def fOccur(arr,low,high):
    if(low>high):
        return -1
    mid=(low+high)//2
    if arr[mid]>x:
        return fOccur(arr,low,mid-1)
    elif arr[mid]<x:
        return fOccur(arr,mid+1,high)
    else:
        if mid==0 or arr[mid-1] != arr[mid]:
            return mid
        else:
            return fOccur(arr,low,mid-1)
n=int(input())
li=list(map(int,input().strip().split()))[:n]
x=int(input())
y=firstOccurence(li,n,x)
print(y)
z=fOccur(li,0,n)
print(z)

