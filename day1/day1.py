with open("input.txt", "r") as f:
    data = f.readlines()



l, r = zip(*[x.split() for x in data])

l = list(l)
r = list(r)


l_s = l.sort()
r_s = r.sort()

res = 0

for i, x in enumerate(l):
    res = res + abs(int(x) - int(r[i]))


print(res)


#find numbers in left list in right list, multiply number by occurences

res = 0

for i, x in enumerate(l):
    res = res + int(x) * r.count(x)

print(res)