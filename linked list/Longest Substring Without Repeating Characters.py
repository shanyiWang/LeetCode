'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        cur, start = 0, 0
        long_length = 0
        record = set()
        while cur < len(s):
            if s[cur] not in record:
                record.add(s[cur])
                long_length = max(long_length, len(record))
            else:
                print(s[start] + '  ' + s[cur])
                while s[start] != s[cur]:
                    record.remove(s[start])
                    start += 1
                start += 1
            cur += 1
        return long_length

    def lengthOfLongestSubstring1(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
