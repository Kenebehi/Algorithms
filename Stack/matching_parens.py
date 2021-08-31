def matching_parens(parens):
    stack = []
    for paren in parens:
        if paren == "(" or parens == "[":
            stack.append(paren)
        elif paren == ")" or parens == "]":
            if stack.pop() == paren:
                return False

    return True


# parens = ["([])", "[)"]
# for paren in parens:
#     print(matching_parens(parens))

parens = "([])"
print(matching_parens(parens))
