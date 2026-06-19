class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0
        for i in nums:
            if (i-1) not in store:
                curr = i
                count = 1
                while (curr+1) in store:
                    count+=1
                    curr+=1
                longest=max(longest,count)
        return longest
                