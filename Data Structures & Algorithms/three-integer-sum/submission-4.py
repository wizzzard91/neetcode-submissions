class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums) - 2): # skip last 2
            if nums[i] > 0: # sum always will give positive
                break
            if i > 0 and nums[i] == nums[i-1]: # was processed
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 > 0:
                    k -= 1
                elif sum3 < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return result
