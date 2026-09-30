class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we need to find jagged part of array and always throw the sorted one
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                # left part of array is sorted, => min in the right
                l = m + 1
            else:
                r = m - 1

        return res