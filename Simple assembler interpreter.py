# This is the first part of this kata series. Second part is here.

# We want to create a simple interpreter of assembler which will support the following instructions:

# mov x y - copies y (either a constant value or the content of a register) into register x
# inc x - increases the content of the register x by one
# dec x - decreases the content of the register x by one
# jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant), but only if x (a constant or a register) is not zero
# Register names are alphabetical (letters only). Constants are always integers (positive or negative).

# Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

# The function will take an input list with the sequence of the program instructions and will execute them. The program ends when there are no more instructions to execute, then it returns a dictionary with the contents of the registers.

# Also, every inc/dec/jnz on a register will always be preceeded by a mov on the register first, so you don't need to worry about uninitialized registers.

# Example
# simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a'])

# ''' visualized:
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a
# ''''
# The above code will:

# set register a to 5,
# increase its value by 1,
# decrease its value by 2,
# then decrease its value until it is zero (jnz a -1 jumps to the previous instruction if a is not zero)
# and then increase its value by 1, leaving register a at 1
# So, the function should return

# {'a': 1}
# This kata is based on the Advent of Code 2016 - day 12

def simple_assembler(program):
    result_dict = {}
    instruction = []
    i = 0
    while i < len(program):
        instruction = program[i]
        argumets = instruction.split()
        instr, x, y = (instruction+ ' 0').split()[:3]
        if argumets[0] == 'mov':
            try:
                result_dict[argumets[1]] = int(argumets[2])
            except ValueError:
                result_dict[argumets[1]] = result_dict[argumets[2]]
        elif argumets[0] == 'inc':
            result_dict[argumets[1]] += 1
        elif argumets[0] == 'dec':
            result_dict[argumets[1]] -= 1
        elif  argumets[0] == 'jnz':
            if (argumets[1].isdigit() and argumets[1] != '0') or (argumets[1].isalpha() and result_dict[argumets[1]] != 0):
                i += int(argumets[2]) - 1 #-1 becouse we incremet it in the next line
        i += 1
    return result_dict

    
# def simple_assembler(program):
#     d, i = {}, 0
#     while i < len(program):
#         cmd, r, v = (program[i] + ' 0').split()[:3]
#         if cmd == 'inc': d[r] += 1
#         if cmd == 'dec': d[r] -= 1        
#         if cmd == 'mov': d[r] = d[v] if v in d else int(v)
#         if cmd == 'jnz' and (d[r] if r in d else int(r)): i += int(v) - 1
#         i += 1
#     return d


code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
print(simple_assembler(code.splitlines()))