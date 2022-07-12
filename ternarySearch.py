# recursive version
def ternarySearch(arr,l,r,x):
    if r>=l:
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        # checking at mid1
        if arr[mid1]==x:
            return mid1
        #  hecking at mid2
        if arr[mid2]==x:
            return mid2
        # x lies before mid1
        if x<arr[mid1]:
            return ternarySearch(arr,l,mid1-1,x)
        # x lies after mid2
        elif x>arr[mid2]:
            return ternarySearch(arr,mid2+1,r,x)
        # if x lies between mid1 and mid2
        else:
            return ternarySearch(arr,mid1+1,mid2-1,x)
    # if x is not present
    return -1
# iterative version
def ternarySearchIterative(arr,n,x):
    l=0
    r=n-1
    while l<=r:
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if arr[mid1]==x:
            return mid1
        if arr[mid2]==x:
            return mid2
        if x<arr[mid1]:
            r=mid1-1
        elif x>arr[mid2]:
            l=mid2+1
        else:
            l=mid1+1
            r=mid2-1
    return -1
num=6
li=[1,2,3,4,5,6]

print(ternarySearch(li,0,5,num))

print(ternarySearchIterative(li,6,num))