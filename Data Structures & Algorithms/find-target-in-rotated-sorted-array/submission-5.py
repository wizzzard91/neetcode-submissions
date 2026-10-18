class Solution:
    def search(self, n: List[int], target: int) -> int:
        l, r = 0, len(n) - 1

        while l <= r:
            if n[l] == target:
                return l

            if n[r] == target:
                return r

            mid = (l + r) // 2
            if n[mid] == target:
                return mid
            
            if n[l] < n[mid]:
                if n[l] < target < n[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif n[mid] < n[r]:
                if n[mid] < target < n[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                return -1

        return -1