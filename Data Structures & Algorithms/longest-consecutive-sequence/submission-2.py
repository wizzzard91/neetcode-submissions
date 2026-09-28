class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxlen = 0

        for n in numsSet:
            if n - 1 not in numsSet: # count amount of consecutives
                i = 0
                while n + i in numsSet:
                    i += 1
                maxlen = max(maxlen, i)
        return maxlen
                