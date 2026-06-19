class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lis = list(nums)
        for i in nums:
            lis.append(i)
        return lis