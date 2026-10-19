class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minValue = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                minValue = min(minValue, nums[l])
                return minValue

            mid = (l + r) // 2
            minValue = min(minValue, nums[mid])

            if nums[l] <= nums[mid]:
                # left side straight => right sight jagged
                l = mid + 1
            else:
                r = mid - 1
        return minValue
