def binarySearch(li,si,hi,x):
    if si>hi:
        return -1
    mid=(si+hi)//2
    if li[mid]==x:
        return mid
    elif li[mid]>x:
        return binarySearch(li,mid+1,hi,x)
    else:
        return binarySearch(li,si,mid-1,x)
    return -1
li=[1,2,3,4,5,6,7]
x=4
print(binarySearch(li,0,6,x))

