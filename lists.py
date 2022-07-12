n=int(input())
a=list(map(int,input().strip().split()))[:n]
print(a)
sum=0
for i in range(0,n):
   sum+=a[i]
print(sum)
# linear search in list
def linearSearch(li,ele):
   for i in range(len(li)):
      if li[i]==ele:
         return i
   return -1
m=int(input())
#lst=list(map(int,input().strip().split()))[:m]
lst=[int(x) for x in input().split()][:m]
ele=int(input())
print(ele,"is at index:",linearSearch(lst,ele))