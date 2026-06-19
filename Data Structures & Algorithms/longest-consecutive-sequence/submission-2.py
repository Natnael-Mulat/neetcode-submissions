class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has=defaultdict(int)
        longest=0
        for i in nums:
            if not has[i]:
                has[i] = has[i-1] + has[i+1] +1
                has[i-has[i-1]] = has[i]
                has[i+has[i+1]] = has[i]
                longest = max(longest, has[i])
        return longest