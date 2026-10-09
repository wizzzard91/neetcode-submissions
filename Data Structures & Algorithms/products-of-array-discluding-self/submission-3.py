class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        productOfPreviousNumbers = 1
        for i in range(0, len(nums)):
            result[i] = productOfPreviousNumbers
            productOfPreviousNumbers = productOfPreviousNumbers * nums[i]
        
        productOfPreviousNumbers = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * productOfPreviousNumbers
            productOfPreviousNumbers = productOfPreviousNumbers * nums[i]
        
        return result
