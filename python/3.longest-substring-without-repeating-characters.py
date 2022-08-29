#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        now_s = ""
        for i in range(len(s)):
            if s[i] in now_s:
                now_s = now_s[now_s.find(s[i])+1:]
                now_s += s[i]
            else:
                now_s += s[i]
            print(now_s)
            ans = max(ans, len(now_s))   
        
        return ans
        
# @lc code=end

