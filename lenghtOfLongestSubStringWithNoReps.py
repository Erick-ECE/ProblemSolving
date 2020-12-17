# length longest substring wihtout repeting characters
'''
Example1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example2:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

#slidig window solution
def lengthOfLongestSubstring(self, s: str) -> int:
       sub= set()
       i=0
       j=0
       m=0
       while j<len(s):
           if s[j] not in sub:
               sub.add(s[j])
               j+=1
               m=max(len(sub),m)
           else:
               sub.remove(s[i])
               i+=1
       return m
                