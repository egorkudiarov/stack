from Stack import Stack

def is_closed(left, right):
    match (left, right):
        case ('(', ')') | ('[', ']') | ('{', '}'):
            return True
    return False

def check(line):
    stack = Stack()
    for element in line:
        if stack.is_empty():
            stack.push(element)
            continue

        if is_closed(stack.peek(), element):
            stack.pop()
        else:
            stack.push(element)
    
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'