class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # num:count
        mp = {} # count: [num]
        for n in range(1, len(nums) + 1):
            mp[n] = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num, count in freq.items():
            mp[count].append(num)
        result = []
        for ns in reversed(mp.values()):
            for n in ns:
                if k > 0:
                    result.append(n)
                    k = k - 1
            if k == 0:
                return result
        return []
        