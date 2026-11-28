class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {

        function isAlphaNum(char) {
            return /^[a-z0-9]$/i.test(char);
        }

        let left = 0
        let right = s.length - 1
        
        while (left < right) {
            if (isAlphaNum(s[left]) == false) {
                left += 1
                continue
            }
            if (isAlphaNum(s[right]) == false) {
                right -= 1
                continue
            }
            if (s[left].toLowerCase() !== s[right].toLowerCase()) {
                return false
            }
            left += 1
            right -= 1
        }

        return true



    }
}
