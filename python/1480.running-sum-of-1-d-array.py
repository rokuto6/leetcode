#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        sum = 0
        for n in nums:
            sum += n
            ans.append(sum)
        return ans
# @lc code=end

