class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for n in nums:
            frequencyMap[n] = frequencyMap.get(n, 0) + 1
        
        top = sorted(frequencyMap, key=lambda x: frequencyMap[x], reverse=True)
        return top[:k]
