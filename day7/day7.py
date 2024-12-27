from functools import reduce
from operator import mul
from itertools import product

with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

#part1
#a line is an equation in the form result : inputs
#inputs can be either added or multiplied
#find equations with true combinations of input and sum the results of the equations
operators = ['+', '*']

def evaluate_expr(values, ops):
    val = values[0]
    for i, op in enumerate(ops, start=1):
        if op == '+':
            val += values[i]
        elif op == '*':
            val *= values[i]
    return val

total_sum = 0

for line in data:
    result, inputs = line.split(":")
    inputs = [int(x) for x in inputs.split()]
    result = int(result)

    #check if result is the sum of the inputs
    if result == sum(inputs):
        total_sum += result
        continue
    #check if result is the product of all inputs
    elif result == reduce(mul, inputs):
        total_sum += result
        continue
    else:
        #check if there is any combination of multiplication and addition that results in the result
        #assume there is no limit on how many input values exist
        found = False
        for combo in product(operators, repeat=len(inputs)-1):
            if evaluate_expr(inputs, combo) == result:
                total_sum += result
                found = True
                break

        if not found:
            pass

print(total_sum)

#part2
#add third operator | which concatenates the inputs e.g., 12 345 -> 12345

operators = ['+', '*', '|']

def evaluate_expr(values, ops):
    val = values[0]
    for i, op in enumerate(ops, start=1):
        if op == '+':
            val += values[i]
        elif op == '*':
            val *= values[i]
        elif op == '|':
            val = int(str(val) + str(values[i]))
    return val

total_sum = 0

for line in data:
    result, inputs = line.split(":")
    inputs = [int(x) for x in inputs.split()]
    result = int(result)

    #check if result is the sum of the inputs
    if result == sum(inputs):
        total_sum += result
        continue
    #check if result is the product of all inputs
    elif result == reduce(mul, inputs):
        total_sum += result
        continue
    elif result == int("".join(map(str, inputs))):
        total_sum += result
        continue
    else:
        #check if there is any combination of multiplication and addition that results in the result
        #assume there is no limit on how many input values exist
        found = False
        for combo in product(operators, repeat=len(inputs)-1):
            if evaluate_expr(inputs, combo) == result:
                total_sum += result
                found = True
                break

        if not found:
            pass

print(total_sum)
