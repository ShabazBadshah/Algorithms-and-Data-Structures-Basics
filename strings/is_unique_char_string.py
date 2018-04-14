def is_unique_char_string(string):
    str_hash = {}
    for letter in string:
        if letter in str_hash:
            return False
        else:
            str_hash[letter] = ''
    return True

print (is_unique_char_string("abc"))
print (is_unique_char_string(""))
print (is_unique_char_string("racecar"))
print (is_unique_char_string("aA"))
print (is_unique_char_string("potato"))