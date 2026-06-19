class Solution:
    def confusingNumber(self, n: int) -> bool:
        dic = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        num = ""
        for i in str(n):
            if i not in dic:
                return False
            num+=dic[i]
        return int(num[::-1]) != n

            
        