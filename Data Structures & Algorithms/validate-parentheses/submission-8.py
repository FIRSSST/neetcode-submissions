class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {
            ']':'[',
            ')':'(',
            '}':'{',
        }
        """
            s = ([{
        """
        stack = [] 
        for char in s:
            print(stack)
            if char not in d:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                twin = stack.pop() 
                if not d[char] == twin:
                    return False 
        
        if len(stack) == 0:
            return True 
        
        return False
        
