def categorize_ingredients(file):
    fin = open(file)
    fresh_ids = []
    count = 0
    for line in fin:
        line = line.strip()
        if '-' not in line and line != '':
            line = int(line)
            for pair in fresh_ids:
                if line >= int(pair[0]) and line <= int(pair[1]):
                    count += 1
                    break
        elif '-' in line:
            rng = line.split('-')
            fresh_ids.append(rng)
    return count
#print(categorize_ingredients('input5'))

def categorize_ingredients_pt_2(file):
    fin = open(file)
    fresh_ids = []
    new_ranges = []
    count = 0
    for line in fin:
        line = line.strip()
        if line == '':
            break
        rng = line.split('-')
        fresh_ids.append(rng)
    fresh_ids = sorted(fresh_ids, key = lambda x: int(x[0]))
    cur = fresh_ids[0]
    start = cur[0]
    end = cur[1]
    for i in range(1,len(fresh_ids)):
        nextid = fresh_ids[i]
        nexts = nextid[0]
        nexte = nextid[1]
        if int(nexts) <= int(end)+1:
            end = max(int(end), int(nexte))
            pair = [start,end]
        else:
            new_ranges.append([start,end])
            start = nexts
            end = nexte
    new_ranges.append([start,end])
    return sum_ids(new_ranges)

def sum_ids(ids):
    sum_of_ids = 0
    for item in ids:
        init = int(item[0])
        final = int(item[1])
        sum_of_ids += final-init+1
    return sum_of_ids
print(categorize_ingredients_pt_2('input5'))
