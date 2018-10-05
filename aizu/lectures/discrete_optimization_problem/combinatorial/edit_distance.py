#! python3

def levenshtein(str1, str2):
    if len(str1) == 0 or len(str2) == 0: return max(len(str1), len(str2))
    # init
    dp = [[None for i in range(len(str2)+1)] for i in range(len(str1)+1)]
    for i in range(len(str1)+1): dp[i][0] = i
    for j in range(len(str2)+1): dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            val = dp[i-1][j-1] if str1[i-1] == str2[j-1] else dp[i-1][j-1]+1
            dp[i][j] = min(val, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp[-1][-1]

s1 = input()
s2 = input()

print(levenshtein(s1, s2))
