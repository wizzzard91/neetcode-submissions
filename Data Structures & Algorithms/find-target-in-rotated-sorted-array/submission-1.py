class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # we need to understand what part should we throw away by comparing l, m, r with target
        l, r = 0, len(nums) - 1
        result = -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                # left side grows
                if nums[l] <= target < nums[m]:
                    # target in the left side
                    r = m - 1
                else:
                    # target in the right side
                    l = m + 1
            else:
                # left side not grows
                if nums[m] < target <= nums[r]:
                    # target in the growing right side
                    l = m + 1
                else:
                    # target in the left jagged side
                    r = m - 1

        return result