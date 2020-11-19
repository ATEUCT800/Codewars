# For a given string s find the character c (or C) with longest consecutive repetition and return:

# (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

# For empty string return:

# ('', 0)
# Happy coding! :)

# import re

# def longest_repetition(chars):
#     if not chars: return ("", 0)
    
#     longest = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
#     return (longest[1], len(longest[0]))

def longest_repetition(chars):
    max = 0
    length = 1
    max_char = ''
    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:  length += 1
        else:   length = 1
        if length > max:    max, max_char = length, chars[i-1]

    return max_char, max


print(longest_repetition('bbbaaabaaaa'))