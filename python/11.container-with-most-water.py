#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
# 
# 14:15-

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        wall = [0, len(height)-1]
        ans = min(height[0], height[-1])*(len(height)-1)
        while wall[0] != wall[1]:
            if height[wall[0]] <= height[wall[1]]:
                wall[0] += 1
            else:
                wall[1] -= 1
            ans = max(ans, min(height[wall[0]], height[wall[1]])*(wall[1]-wall[0]))
        
        return ans
            

# @lc code=end

