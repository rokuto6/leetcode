#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomdict = {}
        magadict = {}
        for s in ransomNote:
            print(s)
            if s in ransomdict:
                ransomdict[s] = ransomdict[s] + 1
            else:
                ransomdict[s] = 1
        for s in magazine:
            print(s)
            if s in magadict:
                magadict[s] = magadict[s] + 1
            else:
                magadict[s] = 1
        
        for key in ransomdict.keys():
            if key not in magadict:
                return False
            elif ransomdict[key] > magadict[key]:
                return False
        
        return True
        
# @lc code=end

