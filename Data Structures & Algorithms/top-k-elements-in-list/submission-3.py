class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = defaultdict(int)
        for n in nums:
            frequencyMap[n] += 1
        top = sorted(frequencyMap, key=lambda x: frequencyMap[x], reverse=True)
        return top[:k]