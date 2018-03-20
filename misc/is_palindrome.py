def is_palindrome_iter(word):
    if (len(word) <= 1):
        return True

    for i in range(len(word)):
        if (word[i] != word[len(word) - i - 1]):
            return False

    return True


def is_palindrome_rec(word):
    if (len(word) <= 1):
        return True
    
    if (word[0] != word[len(word) - 1]):
        return False
    
    return is_palindrome_rec(word[1:len(word) - 1])

print(is_palindrome_iter("foof"))
print(is_palindrome_iter("")) 
print(is_palindrome_iter("a")) 
print(is_palindrome_iter("racecar"))
print(is_palindrome_iter("potato"))
print(is_palindrome_iter("ABC"))

print(is_palindrome_rec("foof"))
print(is_palindrome_rec("")) 
print(is_palindrome_rec("a")) 
print(is_palindrome_rec("racecar"))
print(is_palindrome_rec("potato"))
print(is_palindrome_rec("ABC"))