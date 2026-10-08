class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet to count not only numbers, but also it's neighbors
        numSet = set(nums)
        longest = 0
        for n in numSet:
            # if we have n-1, skip - it's not the start of seq
            # if no n-1, means we need to count all the subsequent
            if n-1 not in numSet:
                i = 1
                while n + i in numSet:
                    i += 1
                longest = max(longest, i)
        return longest
                
