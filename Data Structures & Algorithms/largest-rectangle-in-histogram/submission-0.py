class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, (i-index)*height)
                start = index
            stack.append([start,h])
        while stack:
            new_i, new_h = stack.pop() 
            area = max(area, (len(heights) - new_i)*new_h)
        return area