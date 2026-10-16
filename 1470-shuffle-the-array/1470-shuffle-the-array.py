class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        res = [] #empty array
        for r in range(n,len(nums)):
            res.append(nums[l])
            res.append(nums[r])
            l += 1

        return res


