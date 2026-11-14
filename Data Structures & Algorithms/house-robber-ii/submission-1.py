class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLinear(arr):
            memo = {}

            def dp(i):
                if i >= len(arr):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = arr[i] + max(dp(i + 2), dp(i + 3))
                return memo[i]

            return max(dp(0), dp(1))

        return max(robLinear(nums[:-1]), robLinear(nums[1:]))