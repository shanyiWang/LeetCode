class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0] * len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if ans == "" or max_length < j - i + 1:
                        ans = s[i: j + 1]
                        max_length = j - i + 1
        return ans
