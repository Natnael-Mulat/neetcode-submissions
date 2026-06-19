class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        ans = ""
        for c in range(len(first)):
            for i in range(1,len(strs)):
                if c >= len(strs[i]):
                    return ans
                if first[c] != strs[i][c]:
                    return ans
            ans+=first[c]
        return ans
