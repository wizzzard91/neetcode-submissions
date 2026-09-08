class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}  # ключ: число, значение: частота
        for n in nums:
            if n in frequencyMap:
                frequencyMap[n] = frequencyMap[n] + 1
            else:
                frequencyMap[n] = 1

        sortedNums = sorted(frequencyMap, key=lambda x: frequencyMap[x], reverse=True)

        return sortedNums[:k]