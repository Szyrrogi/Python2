def is_balanced(expression: str) -> bool:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in brackets.values(): 
            stack.append(char)
        elif char in brackets: 
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack 