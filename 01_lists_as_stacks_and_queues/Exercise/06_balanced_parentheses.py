def check_balance(expression):
    stack = []
    for char in expression:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            curr_char = stack.pop()
            if curr_char == '(':
                if char != ")":
                    return False
            if curr_char == '{':
                if char != "}":
                    return False
            if curr_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    else:
        return True


sequence = input()

if check_balance(sequence):
    print("YES")
else:
    print("NO")