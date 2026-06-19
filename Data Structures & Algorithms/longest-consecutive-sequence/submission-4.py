class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        store = set(nums)
        for i in nums:
            curr , streak = i, 0
            while curr in store:
                streak+=1
                curr+=1
            ans = max(ans, streak)
        return ans