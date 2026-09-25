class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        runningProduct = 1
        for i in range(0, len(nums), 1):
            products[i] = runningProduct
            runningProduct = runningProduct * nums[i]

        runningProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] = runningProduct * products[i]
            runningProduct = runningProduct * nums[i]

        return products

            