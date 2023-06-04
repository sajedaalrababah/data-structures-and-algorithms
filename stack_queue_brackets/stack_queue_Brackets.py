def validate_brackets(s):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0 or bracket_pairs[stack.pop()] != char:
                return False

    return len(stack) == 0


print(validate_brackets("()"))  # True
print(validate_brackets("({[]})"))  # True
print(validate_brackets("({[})"))  # False
print(validate_brackets("({)"))  # False
