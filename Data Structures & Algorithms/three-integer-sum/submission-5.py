class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()
        res = []

        for i in range(len(n) - 2):
            if n[i] > 0:
                break
            if i > 0 and n[i-1] == n[i]:
                continue # already processed

            j, k = i + 1, len(n) - 1
            while j < k:
                sum3 = n[i] + n[j] + n[k]
                if sum3 > 0:
                    k -= 1
                elif sum3 < 0:
                    j += 1
                else:
                    res.append([n[i], n[j], n[k]])
                    j += 1
                    k -= 1
                    while n[j] == n[j-1] and j < k:
                        j += 1

        return res
