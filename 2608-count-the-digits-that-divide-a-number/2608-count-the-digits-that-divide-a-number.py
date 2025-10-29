class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        count = 0
        while(n > 0):
            rem = n % 10
            if num % rem == 0:
                count += 1
            n = n// 10
        return count


        