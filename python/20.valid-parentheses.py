#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        for c in s:
            if c == ")":
                if not lst:
                    return False
                if lst[-1] != "(":
                    return False
                lst.pop(-1)
            elif c == "}":
                if not lst:
                    return False
                if lst[-1] != "{":
                    return False
                lst.pop(-1)
            elif c == "]":
                if not lst:
                    return False
                if lst[-1] != "[":
                    return False
                lst.pop(-1)
            else:
                lst.append(c)
        
        if lst:
            return False
        
        return True

# @lc code=end

