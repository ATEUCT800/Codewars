# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

# Your task is to process a string with "#" symbols.

# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

# def clean_string(s):
#     while  '#' in s and re.findall('\w', s):
#         s =  re.sub(r'(\w#)', '', s)
#     if '#' in s:
#         return ''
#     return s
def clean_string(s):
    while '#' in s:
        index = s.find('#')
        s = s[:index - 1 if index - 1 >= 0 else 0] + s[index + 1:]
    return s

print(clean_string('?t######n#!gFM#E\\'))