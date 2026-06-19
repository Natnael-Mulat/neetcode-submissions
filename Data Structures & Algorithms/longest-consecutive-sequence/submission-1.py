class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0
        for i in nums:
            if (i-1) not in store:
                count = 1
                while (i+count) in store:
                    count+=1
                longest=max(longest,count)
        return longest
                