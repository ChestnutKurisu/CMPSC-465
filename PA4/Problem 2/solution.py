# Param Somane (pss5256)
x = input()
n = len(x)
lengthOfLongestSubsequence = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    lengthOfLongestSubsequence[i][i] = 1
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if not x[i] == x[j]:
            lengthOfLongestSubsequence[i][j] = max(lengthOfLongestSubsequence[i + 1][j],
                                                   lengthOfLongestSubsequence[i][j - 1])
        else:
            lengthOfLongestSubsequence[i][j] = 2 + lengthOfLongestSubsequence[i + 1][j - 1]
print(lengthOfLongestSubsequence[0][n - 1])
