from pymathexp.op import operations
from pymathexp.op import Op

def shunting_yard(exp: str):

    rpn_out = []
    op_stack = []
    current_token = ""
    index = 0

    for char in exp:
        # Check if char is operator or paren.
        if char not in operations and char not in ["(", ")"]:
            current_token += char
            # Check if next char exists
            if len(exp) > index + 1:
                next_char = exp[index + 1]
                # Push token to output if next char is operator or paren.
                if next_char in operations or next_char in ["(", ")"]:
                    if current_token in operations:
                        op_stack.append(current_token)
                    else:
                        rpn_out.append(current_token)
                    current_token = ""
        else:
            if char == "(":
                op_stack.append("(")
            elif char == ")":
                # Pop operators from op_stack and push to output until meeting (
                while op_stack[-1] != "(":
                    popped = op_stack.pop()
                    rpn_out.append(popped)
                op_stack.pop()
            elif char == "," or char == " ":
                pass
            else:
                op = operations.get(char)
                # Repeat until op_stack is empty or meet break
                while len(op_stack) > 0:
                    op_before = op_stack[-1]
                    if op_before != "(" and op_before != ")":
                        op_before = operations.get(op_before)
                        # FIXME: Clean up this mess
                        if op.precedence == -1:
                            op.precedence = 10000000
                        if op_before.precedence == -1:
                            op_before.precedence = 10000000
                        if (op.precedence < op_before.precedence or
                            op.precedence == op_before.precedence and
                            op.associativity == 0):
                            rpn_out.append(op_stack.pop())
                        else:
                            break
                    else:
                        break
                op_stack.append(char)

        # Events at the last character
        if index == len(exp) - 1:
            if current_token != "":
                rpn_out.append(current_token)
            op_stack.reverse()
            rpn_out.extend(op_stack)
        index += 1
    return rpn_out