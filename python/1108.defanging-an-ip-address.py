#
# @lc app=leetcode id=1108 lang=python
#
# [1108] Defanging an IP Address
#

# @lc code=start
import copy
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        count = 0
        ans = copy.copy(address)
        for i, c in enumerate(address):
            if c == ".":
                ans = ans[:i+count] + "[" + "." + "]" + ans[i+1+count:]
                count += 2
            
        return ans
        
# @lc code=end

