class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lis = [0] * (2*len(nums))
        for i in range(len(nums)):
            lis[i] = nums[i]
            lis[i+len(nums)] = nums[i]
        return lis