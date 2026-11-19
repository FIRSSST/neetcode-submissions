from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_map = Counter(t)
        required_length = len(t_map) # unique chars in t
        seen = {} # seen "visibility window" of R - L pointers
        left = 0
        min_length = float("inf")
        start_end = (0,0)
        
        formed = 0

        for right,char in enumerate(s):
            seen[s[right]] = seen.get(s[right], 0) + 1

            if s[right] in t_map and seen[s[right]] == t_map[s[right]]: # if length of the char is same
                formed += 1
            
            while formed == required_length:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start_end = (left, right + 1)

                seen[s[left]] -= 1

                if s[left] in t_map and seen[s[left]] < t_map[s[left]]:
                    formed -= 1
                left += 1
        
        if min_length == float("inf"):
            return ""
        
        return s[start_end[0]:start_end[1]]

        