class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            t = str(tokens[i])
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(tokens[i]))

        return stack[0]