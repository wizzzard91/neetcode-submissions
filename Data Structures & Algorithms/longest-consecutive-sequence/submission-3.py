class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        
        for n in numsSet:
            if n - 1 not in numsSet:
                i = 1
                while n + i in numsSet:
                    i += 1
                longest = max(longest, i)
        return longest