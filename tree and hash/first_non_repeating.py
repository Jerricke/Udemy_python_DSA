def first_non_repeating_char(string):
    mapper = {}
    for char in string:
        mapper[char] = mapper.get(char, 0) + 1
    for char in string:
        if mapper[char] == 1:
            return char
    return None
        
        


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc'))