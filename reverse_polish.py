
notation = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']


def compute_polish_notation(notation):
    stack = []
    for ele in notation:
        if ele in ['+', '-', '*', '/']:
            left = stack.pop()
            right = stack.pop()
            expression = f"{right}{ele}{left}"
            print(f"evaluating expression = {expression}")
            value = int(eval(expression))
            stack.append(value)
        elif isinstance(int(ele), int):
            stack.append(ele)
        print(f"Stack after {ele}: {stack}")
    return stack

print(compute_polish_notation(notation))