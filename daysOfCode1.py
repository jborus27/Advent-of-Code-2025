##worked with annalee

def find_password(file):
    cur = 50
    res = 0
    fin = open(file)
    for line in fin:
        num = int(line[1:])
        if line[0] == 'L':
            temp = cur - num
            if cur - num >= 0:
                cur = cur - num
            else:
                cur = abs(temp%100)
        else:
            if cur+num < 99:
                cur += num
            else:
                temp = cur + num
                cur = temp%100
        if cur == 0:
            res+=1
    return res

def find_password_pt_2(file):
    cur = 50
    res = 0
    fin = open(file)
    for line in fin:
        num = int(line[1:])
        for i in range(0,num):
            if line[0] == 'L':
                cur = (cur-1)%100
            else:
                cur = (cur+1)%100
            if cur == 0:
                res += 1
    return res

print(find_password('input'))
print(find_password_pt_2('input'))
