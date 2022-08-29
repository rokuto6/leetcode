#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
        else:
            return self.subPalindrome(s[0], s[1:], [0])
        
    def subPalindrome(self, c, s, lst):
        if not s:
            return c[lst[0]:]
        else:
            lst_next = []
            for e in lst:
                if e == 0:
                    continue
                if s[0] == c[e-1]:
                    lst_next.append(e-1)
        if s[0] == c[-1]:
            lst_next.append(len(c)-1)
        lst_next.append(len(c))
        s_next = self.subPalindrome(c + s[0], s[1:], lst_next)
        if len(c[lst_next[0]:]+ s[0]) > len(s_next):
            return c[lst_next[0]:]+ s[0]
        else:
            return s_next

# @lc code=end

