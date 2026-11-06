class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        seen = {} #keep track of frequency of chars in s
        max_freq = 0 # keep track of highest occuring char and its count 
        left = 0 # left pointer for sliding window
        max_len = 0 # length of max characters segment

        for right, char in enumerate(s):
            seen[s[right]] = seen.get(s[right], 0) + 1 # update frequency count for this character

            max_freq = max(max_freq, seen[s[right]]) # update max freq if necessary

            # the window length can ever be (right - left) + 1 = k + max_freq, so the most frequent character plus k distinct characters

            while (right - left + 1) - max_freq > k:
                seen[s[left]] -= 1 # move left pointer
                left += 1
            
            max_len = max(max_len, (right - left) + 1)

        return max_len