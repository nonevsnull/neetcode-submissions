class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        water = 0
        while l < r:
            water = max(min(heights[l], heights[r]) * (r - l), water)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return water
    