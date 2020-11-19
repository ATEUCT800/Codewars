# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
import copy

def valid_parentheses(string):
    new_str = copy.deepcopy(string)
    while new_str:
        left = new_str.find('(')
        right = new_str.find(')')
        if left == -1 and right == -1:
            return True
        if left < right and left != -1 and right != -1:
            new_str = new_str.replace('(', "", 1)
            new_str = new_str.replace(')', "", 1)
        else:
            return False
    return True

print(valid_parentheses('hi(hi)()'))