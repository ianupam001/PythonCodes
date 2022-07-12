# bubble Sort
def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[j],arr[i]=arr[i],arr[j]
#selection sort
def selectionSort(arr):
    length=len(arr)
    for i in range(length-1):
        minIdx=i
        for j in range(i+1,length):
            if arr[j]<arr[minIdx]:
                minIdx=j
        arr[i],arr[minIdx]=arr[minIdx],arr[i]

def binarySearch(arr,x):
    #selectionSort(arr)
    bubbleSort(arr)
    print(arr)
    low=0
    high=len(li)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
    return -1

n=int(input())
li=[]
#li=[int(x) for x in input().split()][:n]
li=list(map(int,input().strip().split()))[:n]
x=int(input())
index=binarySearch(li,x)
print(index)