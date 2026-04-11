class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for cha in s:
            if cha in "[{(":
                stack.append(cha)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                
                if cha == ")" and curr != "(":
                    return False
                if cha == "]" and curr != "[":
                    return False
                if cha == "}" and curr != "{":
                    return False
                
        
        return len(stack) == 0