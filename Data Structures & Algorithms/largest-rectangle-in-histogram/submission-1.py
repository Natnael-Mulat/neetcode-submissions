class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, h in enumerate(heights):
            start_index = i
            while stack and stack[-1][1]>h:
                prev_index, height = stack.pop()
                area = max(area, height*(i-prev_index))
                start_index = prev_index
            stack.append([start_index, h])
        for s in stack:
            area = max(area,s[1]*(len(heights)-s[0]))
        return area