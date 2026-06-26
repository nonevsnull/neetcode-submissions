class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [num, count]
        # [count, [num]], static size
        # scan above, start from the tail
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        count_nums = {}
        i = 1
        while(i <= len(nums)):
            count_nums[i] = []
            i = i + 1
        
        for num, count in freq.items():
            count_nums[count].append(num)
        r = []
        for key in reversed(list(count_nums.keys())):
            if count_nums[key] == []:
                continue
            for v in count_nums[key]:
                if k > 0:
                    r.append(v)
                    k = k - 1
            if k == 0:
                return r
        return []