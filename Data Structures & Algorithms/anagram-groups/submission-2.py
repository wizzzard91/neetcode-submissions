class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        tmpContainer = {}

        for s in strs:
            keyArray = [0] * 26
            for c in s:
                charIndex = ord(c) - ord('a')
                keyArray[charIndex] = keyArray[charIndex] + 1
            keyTuple = tuple(keyArray)

            if keyTuple not in tmpContainer:
                tmpContainer[keyTuple] = []

            tmpContainer[keyTuple].append(s)

        for key, value in tmpContainer.items():
            result.append(value)

        return result
