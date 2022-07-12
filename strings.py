str = "Hello World"
count = 0
for i in str:
    if i == "l":
        count += 1
print(count)
count = 0
for i in range(len(str)):
    if str[i] == "l":
        count += 1
print(count)
# in operation
if 'Hel' in str:
    print("Yes it is substr")
else:
    print("It is not a substr")
# not in operation
if 'Hel' not in str:
    print("Its is not a substr")
else:
    print("It is substr")
