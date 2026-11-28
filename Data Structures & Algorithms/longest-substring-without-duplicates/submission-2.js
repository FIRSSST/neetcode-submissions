class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {

        const seen = new Map();
        let left = 0;
        let max_len = 0 

        for (let right = 0; right < s.length; right++) {
            seen.set(s[right], (seen.get(s[right]) ?? 0) + 1)
            while (seen.get(s[right]) > 1) {
                seen.set(s[left], seen.get(s[left]) - 1)
                left += 1
            }

            max_len = Math.max(right - left + 1, max_len)
        }

        return max_len

    }
}
