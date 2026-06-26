class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) and (not s[l].isalpha() and not s[l].isdigit()):
                l = l + 1
            while r >= 0 and (not s[r].isalpha() and not s[r].isdigit()):
                r = r - 1
            print(l, r)
            if l < r and s[l].lower() != s[r].lower():
                return False
            else:
                l = l + 1
                r = r - 1
        return True