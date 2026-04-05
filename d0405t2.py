class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for c in s: 
            if c in ['(', '[', '{']: 
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False 
                if c==')':
                    if stack[-1] != '(': return False 
                    stack.pop() 
                elif c=='}':
                    if stack[-1] !='{': return False 
                    stack.pop() 
                else : 
                    if stack[-1] != '[': return False 
                    stack.pop() 
        return len(stack) == 0
        pass 