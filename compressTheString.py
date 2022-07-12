from sys import stdin
def  getCompressedString(s):
	
	n = len(s)
	answer = ""
	currentCharCount = 1
	answer += s[0]
	
	for i in range(1, n):
		if s[i] == s[i - 1]:
			currentCharCount += 1
			
		else:
			if currentCharCount > 1:
				answer += str(currentCharCount)
				currentCharCount = 1
				
			answer += s[i]

	if currentCharCount > 1:
		answer += str(currentCharCount)
	return answer
# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)