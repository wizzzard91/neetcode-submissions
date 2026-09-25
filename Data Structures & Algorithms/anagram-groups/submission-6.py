class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            result[key].append(s)

        return list(result.values())