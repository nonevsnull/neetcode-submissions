class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        p = 0
        while(p < len(s)):
            end = p
            while(s[end].isdigit()):
                end = end + 1;
            word_s = end + 1
            word_e = end + 1 + int(s[p:end])
            res.append(s[word_s : word_e])
            p = word_e
        
        return res
