class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        m = 0
        for i in nums:
            freq[i] = freq[i] + 1
            m = max(freq[i], m)
        counts = defaultdict(list)
        for i in range(m + 1):
            counts[i] = []

        for num, count in freq.items():
            counts[count].append(num)
        
        result = []
        for cs in reversed(list(counts.values())):
            for c in cs:
                if k > 0:
                    result.append(c)
                    k = k - 1
                else:
                    return result;
        return result
        