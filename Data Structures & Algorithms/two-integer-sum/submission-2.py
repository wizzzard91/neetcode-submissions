class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersMap = {} # contains number: index 
        for i, n in enumerate(nums):
            complement = target - n
            if complement in numbersMap: # means we found complement number to ours before
                # means we can return it's index + current index
                return [numbersMap[complement], i]
            # either way no matter what we need to save current num
            numbersMap[n] = i
        