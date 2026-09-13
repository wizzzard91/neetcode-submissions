class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefixProduct = 1
        for i, n in enumerate(nums):
            res[i] = prefixProduct
            prefixProduct = prefixProduct * n

        postfixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            res[i] = postfixProduct * res[i]
            postfixProduct = postfixProduct * n

        return res

            

