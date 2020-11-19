# Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

# Example:

# Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
# Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.



class Calculator():

    @classmethod
    def evaluate(self, string):
        priorities = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}           
        separated = string.split()
        result = []
        numbers = []
        operators = []
        for op in separated:
            if op.isnumeric():
                numbers.append(op)
            elif op == '(':
                operators.append(op)
            elif op == ')':
                last_operator = operators.pop()
                while last_operator != '(':
                    
            else:
                while operators and priorities[op] <= priorities[operators[-1]]:
                    numbers.append(str(eval(numbers.pop(-2) + operators.pop() + numbers.pop())))
                operators.append(op)
        return str(int(eval(numbers.pop(-2) + operators.pop() + numbers.pop())))



print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))
