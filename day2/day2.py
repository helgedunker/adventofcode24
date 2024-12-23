with open("input.txt", "r") as f:
    lines = f.readlines()


# part 1
#iterate over lines, check if the number sequence is always decreasing or increasing

def check_safety(a):
  diffs = [a[i + 1] - a[i] for i in range(len(a) - 1)]    # build list of differences between consecutive pairs
  if (all(x < 0 and x in range(-3, 0) for x in diffs) or  # all differences are negative and between -3 and -1
      all(x > 0 and x in range(1, 4) for x in diffs)):    # all differences are positive and between 1 and 3
    return True
  else:
    return False

valid_lines = 0

for line in lines:
    a = line.split()
    diffs = [
        int(a[i+1]) - int(a[i]) for i in range(len(a)-1)
    ]
    if check_safety([int(x) for x in a]):
        valid_lines += 1
    else:
       continue
    
print(valid_lines)


# part 2
# allow one bad element in a sequence
valid_lines = 0
for line in lines:
    a = line.split()
    diffs = [
        int(a[i+1]) - int(a[i]) for i in range(len(a)-1)
    ]
    if check_safety([int(x) for x in a]):
        valid_lines += 1
    else:
        for i in range(len(a)):
           temp = a.copy()
           temp.pop(i)
           if check_safety([int(x) for x in temp]):
               valid_lines += 1
               break

print(valid_lines)

        






