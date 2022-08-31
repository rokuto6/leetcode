#
# @lc app=leetcode id=1920 lang=python
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

# @lc code=end

