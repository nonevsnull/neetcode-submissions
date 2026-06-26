class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [0]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefix_prod[i] = prefix
            prefix = prefix * nums[i]
        suffix_prod = [0]*len(nums)
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix_prod[i] = suffix
            suffix = suffix * nums[i]
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix_prod[i] * suffix_prod[i]
        print(res)
        return res