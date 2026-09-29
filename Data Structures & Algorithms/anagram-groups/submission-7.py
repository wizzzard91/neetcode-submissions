class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            key = tuple(chars)
            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())
