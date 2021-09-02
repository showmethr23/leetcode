class Solution:
    def isValid(self, s: str) -> bool:

        # Solution 1

        l = []

        for i in s:
            if i == '(' and (len(l) == 0 or l.pop()!='('):
                l.append(i)
            elif i == ')' and (len(l)==0 or l.pop!='('):
                return False
            elif i == '}' and (len(l)==0 or l.pop!='{'):
                return False
            elif i == ']' and (len(l)==0 or l.pop!='['):
                return False
        if len(l)==0:
            return True
        else:
            return False

        
        # Solution 2

        p = {")":"(","}":"{","]":"["}
        stack=[]
        for i in string:
            if i in p.values():
                stack.append(i)
            else:
                if stack and p[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True 


