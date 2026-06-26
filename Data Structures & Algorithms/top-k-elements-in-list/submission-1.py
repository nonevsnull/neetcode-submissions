class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] = freq[n] + 1
            else:
                freq[n] = 1
        freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
        
        r = []
        for key, v in freq.items():
            r.append(key)
            k = k - 1
            if k <= 0:
                return r
        
        return []
        

        