class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first scan: {num : count}
        # 2nd scan: build {1~n of count: []} then {count:[num]}
        # 3rd scan: output from the end of above
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] = freq[n] + 1
            else:
                freq[n] = 1
        count_num = {}
        n = 1
        while(n <= len(nums)):
            count_num[n] = []
            n = n + 1
        
        for num, count in freq.items():
            count_num[count].append(num)
        
        r = []
        
        for key in reversed(list(count_num.keys())):
            ns = count_num[key]
            for n in ns:
                if k > 0:
                    r.append(n)
                    k = k - 1
            if k == 0:
                return r

            
        
        return r
        

        