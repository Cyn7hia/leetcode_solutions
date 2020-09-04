class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        if length == 0:
            return s
        else:
            out=s[0]
            for pos, alp_i in enumerate(s):
                for pos_j, alp_j in enumerate(s[:pos:-1]):
                    if alp_i==alp_j:
                        l = s[pos:length-pos_j]
                        if l==l[::-1]:
                            out=s[pos:length-pos_j] if length-pos_j-pos > len(out) else out
            return out
