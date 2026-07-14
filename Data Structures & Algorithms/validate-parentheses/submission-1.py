class Solution:
       
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={")":"(","}":"{","]":"["}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if top!=pairs[ch]:
                    return False
        if len(stack) ==0:
            return True           
        return False              