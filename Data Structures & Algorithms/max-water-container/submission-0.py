class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        ans = 0
        while l < r:
            if heights[l] <= heights[r]:
                high = heights[l]
                wide = r-l
                ans = max(ans,high*wide)
                l+=1
            else:
                high = heights[r]
                wide = r-l
                ans = max(ans,high*wide)
                r-=1
        return ans