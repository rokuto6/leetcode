#
# @lc app=leetcode id=1337 lang=python
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        dic_count = {}
        for i in range(len(mat)):
            dic_count[i] = mat[i].count(1)

        lst_count_sorted = sorted(dic_count.items(), key = lambda x:x[1])
        ans = []
        for i in range(k):
            ans.append(lst_count_sorted[i][0])
        
        return ans

        
# @lc code=end

