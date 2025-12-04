from itertools import combinations

def find_largest_voltage(file):
    fin = open(file)
    jolts = []
    for line in fin:
        num1 = 0
        num2 = 0
        largest_index = 0
        line = line.strip()
        nums = list(line)
        for index, num in enumerate(nums):
            if int(num) > int(num1) and index < len(nums)-1:
                num1 = num
                largest_index = index
        for i in range(largest_index+1,len(nums)):
            if int(nums[i]) > int(num2):
                num2 = nums[i]
        final = int(str(num1) + str(num2))
        jolts.append(final)
    return sum(jolts)
#find_largest_voltage('input3')

def find_largest_voltage_pt2(file):
    fin = open(file)
    for line in fin:
        num1 = 0
        place1 = 0
        neww = ""
        count = 0
        for i in reversed(range(11,-1)):
            cur = line[0]
            num2 = int(cur)
            place2 = 0
            for j in range(0,len(fin)-i):
                num2 = int(line[i])
                cur2 = str(int2)
                if cur2 > int2:
                    num2 = cur2
                    place2 = j
            neww += cur2
            holder = line[place2+1]
            line = holder
        count += int(neww)
print(find_largest_voltage_pt2('inputcheck3.txt'))

##annalee helped with this part lol
def find_largest_voltage_pt2(file):
    fin = open(file)
    for line in fin:
        num1 = 0
        place1 = 0
        neww = ""
        count = 0
        for i in reversed(range(11,-1)):
            cur = line[0]
            num2 = int(cur)
            place2 = 0
            for j in range(0,len(fin)-i):
                num2 = line[j]
                cur2 = str(num2)
                if (cur2 > num2):
                    num2 = cur2
                    place2 = j
            neww += num2;
            holder = line[place2+1:]
            line = holder
        count += int(neww);

                
