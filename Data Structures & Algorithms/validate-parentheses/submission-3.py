class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '[':']',
            '{':'}',
            '(':')',
        }
        """
        [[[]]]

        s: [[[
            ]
        """
   
        stack = []

        for i in range (len(s)):
            char = s[i]
            if char in d:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                most_recent = stack.pop()
                if d[most_recent] != char:
                    return False

        if len(stack) != 0:
            return False

        return True