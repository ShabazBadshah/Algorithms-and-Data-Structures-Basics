def reverse_string_iter(string):
    rev_string = ""
    for i in range(len(string) - 1, -1, -1):
        rev_string += string[i]
    return rev_string

def reverse_string_rec(string):
    
    if (string == ""):
        return ""

    if (len(string) == 1):
        return string

    return reverse_string_iter(string[1:]) + string[0]

print(reverse_string_iter("abc"))
print(reverse_string_iter("racecar"))
print(reverse_string_iter(""))
print(reverse_string_iter("abc def hij"))

print("\nRecursive Reverse String\n")
print(reverse_string_rec("abc"))
print(reverse_string_rec("racecar"))
print(reverse_string_rec(""))
print(reverse_string_rec("abc def hij"))
