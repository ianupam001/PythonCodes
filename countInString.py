"""count vowels,consonants,numbers,and special characters"""


def count(string):
    v, c, d, s = 0, 0, 0, 0
    for char in string:
        if ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
            char = char.lower()
            if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
                v += 1
            else:
                c += 1
        elif(char >= '0' and char <= '9'):
            d += 1
        else:
            s += 1
    return v, c, d, s


str = "aansjkashdr4rdmmfdk23e4864421923-jefe ewqj039@."
v, c, d, s = count(str)
print(v, c, d, s)
