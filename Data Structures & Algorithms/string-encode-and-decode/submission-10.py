class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res


    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        result = []
        while r < len(s):
            if s[r] == '#':
                count = int(s[l:r])
                if count == 0:
                    result.append("")
                    l = r + 1
                    r = l
                else:
                    l = r + 1
                    r = l + count
                    result.append(s[l:r])
                    l = r
            r += 1

        return result
