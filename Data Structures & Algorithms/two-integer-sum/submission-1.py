class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need 2 indexes - one for current, one for complement
        # let's store in complement map key: n, value: index
        complementMap = {} 
        for i, n in enumerate(nums):
            complement = target - n
            if complement in complementMap:
                return [complementMap[complement], i]
            if n not in complementMap:
                complementMap[n] = i
