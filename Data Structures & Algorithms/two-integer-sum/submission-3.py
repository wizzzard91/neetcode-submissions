class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idea - we need to find a number and a complement number
        seen = {} # key: seen number, value: index
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                # this means that complement was added already
                return [seen[complement], i]
            seen[n] = i