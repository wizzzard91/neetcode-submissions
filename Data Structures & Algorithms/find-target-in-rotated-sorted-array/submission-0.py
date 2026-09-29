class Solution:
    def search(self, nums: list[int], target: int) -> int:
        result = -1
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                result = m
                break
            if nums[l] == target:
                result = l
                break
            if nums[r] == target:
                result = r
                break
            
                
            if nums[m] > nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return result
        