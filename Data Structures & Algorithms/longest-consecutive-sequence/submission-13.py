class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        longest = 0
        for i in nums:
            if dic[i]==0:
                dic[i] = dic[i-1] + dic[i+1] + 1
                dic[i-dic[i-1]] = dic[i]
                dic[i+dic[i+1]] = dic[i]
                longest=max(longest, dic[i])
        return longest