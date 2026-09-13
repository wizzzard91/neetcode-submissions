class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))) # - explicitrly convert
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        result = []
        stringLength, stringChars, afterDelim = 0, [], False
        for c in s:
            if not afterDelim:
                if c.isnumeric():
                    stringLength = stringLength * 10 + int(c)
                    continue
                elif c == '#':
                    if stringLength == 0:
                        result.append("")
                        continue

                    afterDelim = True
                    continue

            stringChars.append(c)
            stringLength -= 1
            if stringLength == 0:
                afterDelim = False
                result.append(''.join(stringChars))
                stringChars = []

        return result
