#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start

import copy

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targetdiv = copy.copy(nums)
        for i, num in enumerate(targetdiv):
            targetdiv[i] = target - num
        sortednums = sorted(nums)
        sortedtardim = sorted(targetdiv)
        i = 0
        j = 0
        while True:
            if sortednums[i] < sortedtardim[j]:
                i = i+1
                continue
            elif sortednums[i] > sortedtardim[j]:
                j = j+1
                continue
            else:
                if target - sortednums[i] == sortednums[i]:
                    if sortednums[i] == sortednums[i+1]:
                        ans1 = sortednums[i]
                        break
                    else:
                        i = i+1
                        j = j+1
                        continue
                else:
                    ans1 = sortednums[i]
                    break

        ans = []

        for l, ni in enumerate(nums):
            if ni == ans1 or ni == target - ans1:
                ans.append(l)
        
        return ans

        
# @lc code=end

