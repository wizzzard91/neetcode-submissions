class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        presentInList = set()
        for num in nums:
            if num in presentInList:
                return True
            presentInList.add(num)
        return False