class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r, maxarea = 0, len(h) - 1, 0

        while l < r:
            area = min(h[l], h[r]) * (r - l)
            maxarea = max(area, maxarea)
            if h[l] > h[r]:
                r -= 1
            else:
                l += 1
        return maxarea