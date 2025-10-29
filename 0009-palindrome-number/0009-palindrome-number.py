class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y = x
        sum=0
        while y > 0:
            rem =y%10
            y=y//10
            sum= (sum*10)+rem 
        return sum==x