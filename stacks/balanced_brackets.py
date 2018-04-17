def is_balanced(string):
    stack = []
    opening_brackets = "{[("
    closing_brackets = "}])"

    for bracket in string:
        # print bracket
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not len(stack):
                return False
            else:
                curr_bracket = stack.pop()
                matching_closing_bracket = opening_brackets[closing_brackets.index(bracket)]
                if curr_bracket != matching_closing_bracket:
                    return False
        else:
            return False
    return not len(stack)                

print (is_balanced("{[()]}")) #true
print (is_balanced("{[(])}")) #false
print (is_balanced("{{[[(())]]}}")) #true