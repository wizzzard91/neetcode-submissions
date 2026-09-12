class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append('#')
            res.append(string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        lastLength, lastStringChars, delimDetected = 0, [], False
        for char in s:
            if delimDetected is False:
                if char == '#':
                    delimDetected = True
                    if lastLength ==  0:
                        delimDetected = False
                        res.append("")
                    continue
                else:
                    lastLength = lastLength * 10 + int(char)
                    continue
            

            lastStringChars.append(char)
            lastLength -= 1
            if lastLength == 0:
                delimDetected = False
                res.append(''.join(lastStringChars))
                lastStringChars = []
        
        return res
            



            


