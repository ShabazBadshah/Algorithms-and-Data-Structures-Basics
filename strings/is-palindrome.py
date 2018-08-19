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

print("\nIterative Palindrome\n--------------------")
print("foof:    " + str(is_palindrome_iter("foof")))
print("'':      " + str(is_palindrome_iter("")))
print("a:       " + str(is_palindrome_iter("a")))
print("racecar: " + str(is_palindrome_iter("racecar")))
print("potato:  " + str(is_palindrome_iter("potato")))
print("ABC:     " + str(is_palindrome_iter("ABC")))

print ("\nRecursive Palindrome\n--------------------")
print("foof:    " + str(is_palindrome_rec("foof")))
print("'':      " + str(is_palindrome_rec("")))
print("a:       " + str(is_palindrome_rec("a"))) 
print("racecar: " + str(is_palindrome_rec("racecar")))
print("potato:  " + str(is_palindrome_rec("potato")))
print("ABC:     " + str(is_palindrome_rec("ABC")))
