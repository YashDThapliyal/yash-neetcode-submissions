class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        relationships ={
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        # ( ( ( ) ) ) 
        for curr in s:
            stack.append(curr)
            if curr in relationships and stack and stack[len(stack) -2] == relationships[curr]:
                stack.pop()
                stack.pop()

        
        return len(stack) == 0