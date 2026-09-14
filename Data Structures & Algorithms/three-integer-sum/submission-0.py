class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns = sorted(nums)

        tripletsMet = set()
        result = []
        i = 0
        while i < len(ns):
            j = i + 1
            k = len(ns) - 1

            while j < k:
                summ = ns[i] + ns[j] + ns[k]
                if summ > 0:
                    k -= 1
                elif summ < 0:
                    j += 1
                else:
                    if (ns[i], ns[j], ns[k]) not in tripletsMet:
                        result.append([ns[i], ns[j], ns[k]])
                        tripletsMet.add((ns[i], ns[j], ns[k]))
                    k -= 1
                    j += 1

            i += 1
        
        return result