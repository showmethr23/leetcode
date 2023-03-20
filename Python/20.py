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

        # Solution 3

        if len(s) == 0:
            return True
        opcl = dict(('()', '[]', '{}'))
        stack = []
        for idx in s:
            if idx in '([{':
                stack.append(idx)
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        return len(stack) == 0

