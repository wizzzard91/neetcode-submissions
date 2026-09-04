class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        result = []
        for (i, num) in enumerate(nums):
            secondComponent = target - num
            if secondComponent in sumMap:
                firstComponent, j = sumMap.get(secondComponent)
                return [j, i]
            else:
                sumMap[num] = (secondComponent, i)