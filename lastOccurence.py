def lastIndex(li,size,x,currIdx=0):
    if currIdx==size:
        return -1
    if (lastIndex(li,size,x,currIdx+1)==-1) and li[currIdx]==x:
        return currIdx
    else:
        return lastIndex(li,size,x,currIdx+1)

n=int(input())
li=[]
li=list(map(int,input().strip().split()))[:n]
num=int(input())
print(lastIndex(li,n,num))