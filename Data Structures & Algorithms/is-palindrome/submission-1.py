class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1
        
        while left < len(s):
            c1 = s[left].lower()
            c2 = s[right].lower()

            if c1.isalnum() == False:
                left += 1
                continue

            if c2.isalnum() == False:
                right -= 1
                continue    

            if c1 != c2:
                return False
            left += 1
            right -=1
        return True