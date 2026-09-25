class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        l, r, result = 0, 0, []

        while l < len(s) and r < len(s):    # probably last one don't need?
            if s[r] == '#':
                if l == r: # means empty string
                    result.append("")
                    l = l + 1
                    continue
                strlen = int(s[l:r])
                l = r + 1
                string = s[l:l+strlen]
                result.append(string)
                l = l + strlen
                r = l
            else:
                r += 1

        return result
        