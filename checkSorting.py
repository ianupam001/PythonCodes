# def checkSorted(arr):
#     n=len(arr)
#     if n==0 or n==1:
#         return True
#     return arr[0]<=arr[1] and checkSorted(arr[1:])
def sum(arr,n):
    if n==1:
        return arr[0]
    return arr[0]+sum(arr[1:],n)
# recursive linear search
def recSearch( arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return recSearch(arr, l+1, r-1, x)
    
arr=[1,2,3,4,5,6]
print(sum(arr,6))