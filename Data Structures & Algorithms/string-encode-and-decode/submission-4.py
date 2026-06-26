class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "nil"
        ns = []
        for s in strs:
            if s == "":
                ns.append("-1")
            else:
                cs = []
                for c in s:
                    cs.append(ord(c))
                ns.append(','.join(map(str, cs)))
            
        return ';'.join(ns)



    def decode(self, s: str) -> List[str]:
        if s == "nil":
            return []
        strs = s.split(";")
        for i, s in enumerate(strs):
            cs = []
            for c in s.split(","):
                if c == "-1":
                    cs.append("")
                else:
                    cs.append(chr(int(c)))
            strs[i] = ''.join(cs)
        # if len(strs) == 0:
        #     return [""]
        return strs