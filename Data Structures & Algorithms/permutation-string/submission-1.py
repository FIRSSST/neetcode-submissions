from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1) > len(s2):
            return False
        
        s1_map = Counter(s1)
        required_len = len(s1_map)

        seen = {}
        left = 0
        formed = 0 

        for right, char in enumerate(s2):
            seen[s2[right]] = seen.get(s2[right], 0) + 1

            if s2[right] in s1_map and seen[s2[right]] == s1_map[s2[right]]:
                formed += 1
            
            while right - left + 1 > len(s1):

                

                if s2[left] in s1_map and seen[s2[left]] == s1_map[s2[left]]:
                    formed -= 1

                seen[s2[left]] -= 1   
                 
                if seen[s2[left]] == 0:
                    del seen[s2[left]]

                left += 1

            if formed == required_len:
                return True
        
        return False

