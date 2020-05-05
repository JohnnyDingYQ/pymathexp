from pymathexp.op import operations

def rpn_parse(rpn: list) -> float:
    index = 0
    while len(rpn) > index:
        item = rpn[index]
        if item in operations:
            operand_list = []
            # Get the Op object
            op = operations.get(item)
            # Pop the operator
            rpn.pop(index)
            
            # Pop the operand (in REVERSE order) 
            # And add them to operand_list
            for i in range(0, op.num_of_operands):
                operand_list.append(float(rpn.pop(index - (i+1))))
            operand_list.reverse()

            # Insert the result of the operation back to the string
            rpn.insert(index - op.num_of_operands, str(op.function(*operand_list)))

            # Decrease index according to num of items popped
            index -= op.num_of_operands
        index += 1
    # TODO: Result validation and exception raising
    return float(rpn[0])
