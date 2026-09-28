class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        top = sorted(freqMap, key=lambda x: freqMap[x], reverse=True)
        return top[:k]
        