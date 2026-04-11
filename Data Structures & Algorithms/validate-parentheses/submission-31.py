class Solution:
    def isValid(self, s: str) -> bool:
        openers = "({["
        closers = ")}]"
        stack = []
        

        for ch in s:
            if ch in openers:
                stack.append(ch)
            if ch in closers:
                if stack:
                    mostRecent = stack.pop()
                    if ch == ")" and mostRecent != "(":
                        return False
                    elif ch == "]" and mostRecent != "[":
                        return False
                    elif ch == "}" and mostRecent != "{":
                        return False
                else:
                    return False

        return len(stack) == 0
                

