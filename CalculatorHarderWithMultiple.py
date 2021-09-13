class CalculatorHarderWithMultiple:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        ope = "+"
        if not s:
            return 0
        operators = {'+', '-', '*', '/'}
        nums = set(str(x) for x in range(0, 10))

        for i in range(0, len(s)):
            char = s[i]

            if char in nums:
                curr = curr * 10 + int(char)

            if char in operators or i == len(s) - 1:
                if ope == '+':
                    stack.append(curr)

                elif ope == '-':
                    stack.append(-curr)

                elif ope == '*':
                    stack[-1] *= curr

                elif ope == '/':
                    stack[-1] = int(stack[-1] / curr)

                curr = 0
                ope = char

        return sum(stack)

x=CalculatorHarderWithMultiple()
print(x.calculate("3+5/2"))