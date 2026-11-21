from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        t_map = Counter(t)
        required_len = len(t_map)
        seen = {}
        left = 0
        formed = 0
        s_e = (0,0)
        min_length = float("inf")

        for right, char in enumerate(s):
            seen[s[right]] = seen.get(s[right], 0) + 1

            if s[right] in t_map and seen[s[right]] == t_map[s[right]]:
                formed += 1
            
            while formed == required_len:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    s_e = (left, right)
                

                if s[left] in t_map and seen[s[left]] == t_map[s[left]]:
                    formed -= 1
                
                seen[s[left]] -= 1

                
                left += 1
            
        return "" if min_length == float("inf") else s[s_e[0]:s_e[1]+1]