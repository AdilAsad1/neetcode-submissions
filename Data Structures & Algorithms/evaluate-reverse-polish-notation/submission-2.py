class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opp = ['+','-','*','/']

        for i in tokens:
            if i not in opp:
                stack.append(int(i))
            else:
                if i == '+':
                    a = stack[-2] + stack[-1]
                elif i == '-':
                    a = stack[-2] - stack[-1]
                elif i == '*':
                    a = stack[-2] * stack[-1]
                elif i == '/':
                    a = int(stack[-2] / stack[-1])
                    

                stack.pop()
                stack.pop()
                stack.append(a)

        return stack[-1]
                