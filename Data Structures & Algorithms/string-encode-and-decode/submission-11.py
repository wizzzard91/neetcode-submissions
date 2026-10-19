class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        l, r = 0, 0
        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])
                if length == 0:
                    result.append('')
                    l = r + 1
                    r = l
                else:
                    l = r + 1
                    r = l + length
                    result.append(s[l:r])
                    l = r
            else:
                r += 1
        return result
