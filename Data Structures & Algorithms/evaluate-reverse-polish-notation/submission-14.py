class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-/*"

        curr = []
        for cur in tokens:
            if cur in ops:

                a = curr.pop()
                b = curr.pop()

                if cur == "+":
                    curr.append(a+b)
                if cur == "-":
                    curr.append(b-a)
                if cur == "*":
                    curr.append(a*b)
                if cur == "/":
                    curr.append(int(b/a))
            else:
                curr.append(int(cur))


        return curr[0]