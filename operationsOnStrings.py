# function of string
str = "My name is anupam"
li = str.split(',', 2)
print(li)

# replace()
s = "My name is anupam anupam anupam"
# s="My name is anupam"
# we have to store the s in string because strings are immutable
string = s.replace("anupam", "Anupam", 2)
print(string)
# find() -> used to finnd a substr in string it returns the starting index of substr
str = "My name is Anupam Anupam"
index = str.find("Anu", 16, 21)
print(index)
# lower()-> converts all characters into lower case
# upper()-> converts all characters into upper case
str = "My Name Is Anupam"
str = str.lower()
print(str)
str = str.upper()
print(str)
# startswith()
str = "My name is anupam"
ans = str.startswith("anp", 11,)
print(ans)
# replace a character in a string
str = "abcda"
str = str.replace("a", "e")
print(str)
