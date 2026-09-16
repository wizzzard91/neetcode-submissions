class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        l, r = 0, 0
        while l < len(s):
            r = l
            while s[r] != '#' and r < len(s):
                r += 1
            length = int(s[l:r])
            l = r + 1
            result.append(s[l:l + length])
            l = l + length

        return result
