class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sss = []
        for i, v in enumerate(strs):
            sss.append(''.join(sorted(v)))
 
        mp = {}
        for i, v in enumerate(sss):
            if v in mp:
                mp[v].append(i)
            else:
                mp[v] = [i]
        r = []
        for k, v in mp.items():
            load = []
            for i in v:
                load.append(strs[i])
            r.append(load)

        return r