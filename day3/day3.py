import re

with open("input.txt", "r") as f:
    dat = f.read()

#part 1
# from string extract mul(123,456) events via regex as a list

instructions = re.findall(r"mul\((\d+),(\d+)\)", dat)

print(
    sum([int(a) * int(b) for a, b in instructions])
)

#part 2
#check for do() and don't() instruction prior to mul() events
#per default do is present, all mul() events are executed
#don't() cancels the mul() events
res = 0
do_sum = True
for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', dat):
    match x[0]:
        case 'do()':
            do_sum = True
        case 'don\'t()':
            do_sum = False
        
        case _:
            if do_sum:
                res += int(x[1]) * int(x[2])


print(res)