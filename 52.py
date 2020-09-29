def ValidParentheses(string):
    stack = []
    brackets = { ')' : '(', '}' : '{', ']' : '[' }
    for i in string:
        if i in brackets:
            t = stack.pop() if stack else '#'
            if brackets[i] != t:
                return False
        else:
            stack.append(i)
    if len(stack) != 0:
        return False
    else:
        return True

x = input('Enter parentheses expression:')
print(ValidParentheses(x))
