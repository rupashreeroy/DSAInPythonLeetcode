class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = n
        prod = 1
        sum = 0
        while(num > 0):
            rem = num % 10
            prod *= rem
            sum += rem
            num //= 10
        
        return prod - sum

        