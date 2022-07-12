'''def geo(n):
    if n==0:
        return 1
    return 1/pow(2,n)+geo(n-1)'''

'''def isPal(str,st,en):
    if(st>=en):
        return True
    return(str[st]==str[en]) and isPal(str,st+1,en-1)
    
str='aca'
st=0
en=len(str)-1
print(isPal(str,st,en))'''
def sumOfDigits(n):
    if n<=9:
        return n
    else:
      return sumOfDigits(n//10)+n%10
n=12345
print(sumOfDigits(n))