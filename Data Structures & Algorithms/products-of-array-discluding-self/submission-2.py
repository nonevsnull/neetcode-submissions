class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no zero: prod / num
        # 1 zero: all zero except zero pos
        # > 1 zero: all zero
        zero_count = 0
        prod = 1
        for num in nums:
            if num == 0:
                zero_count = zero_count + 1
            else:
                prod = prod * num
            if zero_count == 2:
                return [0]*len(nums)
        r = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    r.append(prod)
                else:
                    r.append(0)
            else:
                r.append(int(prod / num))
        return r
            




