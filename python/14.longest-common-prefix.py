#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = strs[0]
        for s in strs:
            for i in range(len(ans)+1)[::-1]:
                print(s[:i])
                if ans[:i] == s[:i]:
                    ans = ans[:i]
                    break
            print(s)
        return ans
        
# @lc code=end

