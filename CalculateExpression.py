class CalculateExpression:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res = res+(sign * operand)

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res = res+(sign * operand)
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':
                res = res+(sign * operand)
                res = res*(stack.pop()) # stack pop 1, sign
                res = res+(stack.pop()) # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand

x=CalculateExpression()
print(x.calculate("(1+(4+5+2)-3)+(6+8)"))