li = [1, 2, 3, 4]
liNew = []
for ele in li:
    liNew.append(ele**2)
print(liNew)
# above process can be written in just on line
# power of list comprehension
liNew = [ele**2 for ele in li]
print(liNew)
''''if we want square of only even elements'''
liEven = [ele**2 for ele in li if ele % 2 == 0]
print(liEven)
''' If we want only those elements which are multiples of 2 and 3 as well'''
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
li_new = [ele for ele in li if ele % 2 == 0 and ele % 3 == 0]
print(li_new)
'''if we want intersection of two lists then we can use multiple for loops for this'''
li1 = [1, 2, 3, 4, 5, 6]
li2 = [2, 4, 5, 6, 7, 8, 9]
liInter = [ele for ele in li1 for ele2 in li2 if ele == ele2]
print(liInter)
s = "Anupam"
li = [ele for ele in s]
print(li)

li = ['Anupam', 'Anmol', 'Satayam', 'Aarohi']
li_2d = [[s for s in ele] for ele in li]
print(li_2d)
li = [[ i*j for j in range(4)] for i in range(3)]
print(li)