class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefixMultiplication = 1
        for i, n in enumerate(nums):
            result[i] = prefixMultiplication * result[i]
            prefixMultiplication *= n

        postfixMultiplication = 1
        for i in range(len(nums) -1, -1, -1):
            n = nums[i]
            result[i] = postfixMultiplication * result[i]
            postfixMultiplication *= n

        return result
