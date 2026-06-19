class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 0
        for i in nums:
            current = i
            streak = 0
            while current in nums:
                current +=1
                streak +=1
            long = max(long,streak)
        return long