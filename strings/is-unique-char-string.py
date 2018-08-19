def is_unique_char_string(string):
    str_hash = {}
    for letter in string:
        if letter in str_hash:
            return False
        else:
            str_hash[letter] = ''
    return True

def is_unique_char_string_set(string):
    return len(string) == len(set(string))

# Runs in O(n)
print (is_unique_char_string("abc"))
print (is_unique_char_string(""))
print (is_unique_char_string("racecar"))
print (is_unique_char_string("aA"))
print (is_unique_char_string("potato"))

print ("-----Set Implentation-----")
print (is_unique_char_string_set("abc"))
print (is_unique_char_string_set(""))
print (is_unique_char_string_set("racecar"))
print (is_unique_char_string_set("aA"))
print (is_unique_char_string_set("potato"))