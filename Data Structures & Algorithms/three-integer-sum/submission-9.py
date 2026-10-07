class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        # fixing i, calculating sum j + k
        n.sort()
        
        result = []
        for i in range(len(n) - 1):
            if n[i] > 0:
                break # no more sums
            if i > 0 and n[i-1] == n[i]:
                continue # already processed
            
            j, k = i + 1, len(n) - 1
            while j < k:
                sum3 = n[i] + n[j] + n[k]
                if sum3 > 0:
                    # we need to move bigger num to get less sum
                    k -= 1
                elif sum3 < 0:
                    j += 1
                else:
                    # exactly 0
                    result.append([n[i], n[j], n[k]])
                    k -= 1
                    j += 1
                    while n[j-1] == n[j] and j <= k:
                        j += 1
        return result
