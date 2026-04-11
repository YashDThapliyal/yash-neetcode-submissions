class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        endings = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        "]"
        for c in s:
            if c in endings:
                if stack and stack[-1] == endings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                

        if len(stack) == 0:
            return True
        return False