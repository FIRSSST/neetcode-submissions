class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [] 
        for token in tokens:
            if token == "+":
                first = stack.pop()
                second = stack.pop()
                new_num = int (first) + int (second)
                stack.append(new_num)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                new_num = int (second) - int (first)
                stack.append(new_num)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                new_num = int (first) * int(second)
                stack.append(new_num)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                new_num = int (second) / int (first)
                stack.append(new_num)
            else:
                stack.append(token)
            
        return int(stack.pop())
