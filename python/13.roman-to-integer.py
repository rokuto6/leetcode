#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"I" : 1, "V" : 5, "X": 10, "L": 50, 
                "C":100, "D":500, "M":1000}
        dict2 = {"IV" : 4, "IX" : 9, "XL": 40, "XC": 90, 
                "CD":400, "CM":900}
        ans = 0
        i=0
        while i < len(s):
            if i == len(s)-1:
                ans += dict[s[i]]
                i=i+1
            else:
                if s[i]+s[i+1] in dict2:
                    ans += dict2[s[i]+s[i+1]]
                    i=i+2
                else:
                    ans += dict[s[i]]
                    i=i+1
        
        return ans
        
# @lc code=end

