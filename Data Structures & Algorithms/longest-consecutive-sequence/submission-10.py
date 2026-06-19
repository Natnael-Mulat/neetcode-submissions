class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        pointer, streak = nums[0], 0
        ans = 0
        i=0
        while i<len(nums):
            if pointer!=nums[i]:
                pointer, streak = nums[i], 0
            while i<len(nums) and pointer==nums[i]:
                i+=1
            pointer+=1
            streak+=1
            ans = max(ans, streak)
        return ans
            
            
