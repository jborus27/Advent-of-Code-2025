import re
def find_invalid_ids_pt1(file):
    fin = open(file)
    ids = fin.read().split(',')
    invalid_ids = []
    for id in ids:
        range = id.split('-')
        num1 = int(range[0])
        num2 = int(range[1])
        while num1<=int(num2):
            cur = str(num1)
            if len(cur)%2 == 0:
                half1 = cur[:len(cur)//2]
                half2 = cur[len(cur)//2:]
                if half1 == half2:
                    invalid_ids.append(num1)
            num1+=1
    return sum(invalid_ids)

def find_invalid_ids_pt2(file):
    fin = open(file)
    ids = fin.read().split(',')
    invalid_ids = []
    for id in ids:
        rng = id.split('-')
        num1 = int(rng[0])
        num2 = int(rng[1])
        while num1<=int(num2):
            cur = str(num1)
            if(re.match(r"^(\d+?)\1+$", cur)):
                invalid_ids.append(num1)
            num1+=1
    print(invalid_ids)
    return sum(invalid_ids)
print(find_invalid_ids_pt1('input2'))
print(find_invalid_ids_pt2('input2'))
