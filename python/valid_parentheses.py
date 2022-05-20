def isValid(s):
    left_to_right = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    stack = []

    for c in s:
        if c in left_to_right:
            stack.append(c)
        else:
            if len(stack) > 0:
                previous = stack.pop()
                if left_to_right[previous] != c:
                    return False
            else:
                return False

    return len(stack) == 0

data = "{}[]()(){}"
r = isValid(data)
print(r)



