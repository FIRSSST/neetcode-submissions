class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} 
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            seen[s[right]] = seen.get(s[right], 0) + 1

            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len