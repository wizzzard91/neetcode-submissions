class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minValue = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minValue = min(minValue, nums[l])
                break

            m = (l + r) // 2
            minValue = min(minValue, nums[m])

            if nums[l] <= nums[m]:
                # left part is growing -> part size should have min
                l = m + 1
            else:
                # right part is growing -> min on left
                r = m - 1

        return minValue