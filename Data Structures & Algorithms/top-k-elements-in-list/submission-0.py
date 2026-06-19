class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = {}
        for i in nums:
            if i in has:
                has[i] +=1
            else:
                has[i] =1
        sorted_keys = sorted(has, key=has.get)
        return sorted_keys[-k:]
        