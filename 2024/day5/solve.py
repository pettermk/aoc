def verify_rule(data, rule):
    try:
        index1 = data.index(rule[0])
        index2 = data.index(rule[1])
    except ValueError as e: # Rule is not applicable, don't have both numbers here
        return True
    if index1 < index2:
        return True
    return False


# with open('test_input.txt') as f:
with open('input.txt') as f:
    [rules, data] = f.read().split('\n\n') 
    print(rules)
    print(data)
    rules = [r.split('|') for r in rules.split('\n')]

    sum = 0
    for d in data.split('\n'):
        if d == '':
            continue
        d = d.split(',')
        valid = True
        for rule in rules:
            if not verify_rule(d, rule):
                valid = False
                break
        if valid:
            sum += int(d[(len(d) - 1) // 2])

    print(sum)

