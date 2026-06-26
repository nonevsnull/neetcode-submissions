class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {} 
        for s in strs:
            counts = [0]*26
            for c in s:
                counts[ord(c)-ord('a')] = counts[ord(c)-ord('a')] + 1
            key = ','.join(map(str, counts))
            group = mp.get(key, [])
            group.append(s)
            mp[key] = group
        return list(mp.values())