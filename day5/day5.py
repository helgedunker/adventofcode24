with open("input.txt", "r") as f:
    data = f.read()
    rules, updates = data.split("\n\n")
    rules = [x.split("|") for x in rules.split("\n")]
    updates = [x.split(",") for x in updates.split("\n")]

def check_validity(update, rules):
    #based on the rules which are A|B, which means A has to occur prior to B
    #check the update if all rules are followed 
    
    #first filter to relevant rules 
    relevant_rules = [rule for rule in rules if rule[0] in update or rule[1] in update]
    
    #check if all rules are followed
    for a,b in relevant_rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                return False
    
    return True

def create_valid_order(update, rules):
    #based on the rules which are A|B, which means A has to occur prior to B
    #check the update if all rules are followed 
    
    #first filter to relevant rules 
    relevant_rules = [rule for rule in rules if rule[0] in update or rule[1] in update]
    
    #based on the rules, re-order the update 
    i = 0
    while i != len(update):
        i = len(update)
        for a,b in relevant_rules:
            if a in update and b in update:
                if update.index(a) > update.index(b):
                    i -= 1
                    update.pop(update.index(a))
                    update.insert(update.index(b), a)

    return update

res1 = 0
res2 = 0
for update in updates:
    if check_validity(update, rules):
        #add median elements to the result
        res1 += int(update[len(update)//2])
    else:
        #re-order lists and add median to res2
        update_ordered = create_valid_order(update, rules)
        res2 += int(update_ordered[len(update_ordered)//2])


print(res1,res2)

