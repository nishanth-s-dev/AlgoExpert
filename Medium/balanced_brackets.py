def balancedBrackets(string):
    pairs = {'}': '{', ']': '[', ')': '('}

    stack = []
    for s in string:
        if s in pairs:
            if not stack:
                return False
            current = stack.pop()
            if current != pairs[s]:
                return False
        elif s in pairs.values():
            stack.append(s)
    return not stack