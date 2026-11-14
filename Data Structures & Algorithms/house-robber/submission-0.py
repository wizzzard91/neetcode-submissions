class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            maxValue = max(nums[i] + dp(i + 2), nums[i] + dp(i + 3))
            memo[i] = maxValue
            return maxValue
        
        return max(dp(0), dp(1))