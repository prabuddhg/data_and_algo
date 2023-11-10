
paranthesis = {
    '{' : '}',
    '[': ']',
    '(': ')',
    'open' : ['[', '{', '('],
    'close': [']', '}', ')'],
}



input = '({[})'
input = "()[]{}"
input = "(]"

"""
      0
    (  )
  {  }
 [ ]
"""

def validate_input(input):
    stack=[]
    for each_element in range(0, len(input)):
        if input[each_element] in paranthesis['open']:
            print(f" each element in open {input[each_element]}")
            stack.append(input[each_element])
        if input[each_element] in paranthesis['close']:
            poped_element = stack.pop()
            print(f" each element in close {input[each_element]}")
            print(f" poped element {poped_element}")
            #import pdb;pdb.set_trace()
            if paranthesis[poped_element] != input[each_element]:
                stack.append(poped_element)
    if len(stack) == 0:
        return True
    return False

print(validate_input(input))
