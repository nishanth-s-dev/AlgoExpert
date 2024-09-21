def balancedBrackets(string):
    """
    This function checks if the brackets in a given string are balanced.

    Thought Process:
    1. Create a dictionary to define the pairs of brackets.
    2. Initialize an empty stack to keep track of opening brackets.
    3. Iterate through each character in the string:
       - If the character is a closing bracket:
         - Check if the stack is empty; if so, return False (unmatched closing bracket).
         - Pop the top of the stack and check if it matches the corresponding opening bracket; if not, return False.
       - If the character is an opening bracket, push it onto the stack.
    4. After processing all characters, return True if the stack is empty (all brackets matched), otherwise return False.

    This method efficiently uses a stack to ensure brackets are properly nested and matched.
    """
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