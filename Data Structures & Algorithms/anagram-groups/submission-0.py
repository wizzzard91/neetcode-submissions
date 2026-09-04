class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        helperMap = {}

        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in helperMap:
                helperMap[sortedString] = [string]
            else:
                helperMap[sortedString].append(string)
        
        for key, value in helperMap.items():
            result.append(value)

        return result