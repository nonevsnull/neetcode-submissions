class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            mp = [0] * 26
            for c in s:
                mp[ord(c) - ord("a")] = mp[ord(c) - ord("a")] + 1
            dic[",".join(str(n) for n in mp)].append(s)
        return list(dic.values())