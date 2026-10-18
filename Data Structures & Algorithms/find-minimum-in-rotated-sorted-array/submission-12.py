class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:
            if nums[l] < nums[r]: 
                result = min(nums[l], result)
                return result
            
            mid = (l + r) // 2
            result = min(nums[mid], result)
            if nums[l] <= nums[mid]:
                # right side is jagged
                l = mid + 1
            else:
                # left side is jagged
                r = mid - 1

        return result