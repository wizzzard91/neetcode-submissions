class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
            # idea - sort input, then fix one number -> two pointers to get all pairs
            n.sort()

            i, res = 0, []
            for i in range(len(n) - 2):
                # skipping ni > 0
                if n[i] > 0:
                    break
                # skipping i if it was already processed
                if i > 0 and n[i-1] == n[i]:
                    continue

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
                        while n[j-1] == n[j] and j < k:
                            j += 1
            return res
