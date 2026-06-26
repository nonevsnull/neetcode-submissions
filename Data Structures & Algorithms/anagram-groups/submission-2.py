class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            cs = [0]*26
            for c in s:
                cs[ord(c) - ord('a')] = cs[ord(c) - ord('a')] + 1
            key = ','.join(map(str, cs))
            if key in mp:
                mp[key].append(s)
            else:
                mp[key] = [s]
        return list(mp.values())
