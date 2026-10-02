from functools import reduce
class Solution:

    def encode(self, strs: List[str]) -> str:
        return reduce(lambda acc, s: acc + str(len(s)) + '#' + s, strs, '')

    def decode(self, s: str) -> List[str]:
        result = []
        l, r = 0, 0
        while r < len(s):
            if s[r] == '#':
                strLength = int(s[l:r])
                if strLength == 0:
                    result.append("")
                    l = r + 1
                    r = l
                    continue
                l = r + 1
                result.append(s[l:l+strLength])
                l = l+strLength
                r = l
            else:
                r += 1
        return result
