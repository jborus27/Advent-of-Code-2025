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

def find_largest_voltage_pt2(file):
    fin = open(file)
    joltages = []
    for line in fin:
        used = []
        joltages.append(int(find_joltage_helper(0,line, used, "",0)))
    return sum(joltages)

def find_joltage_helper(iteration, line, used, joltage, largest_index):
    largest = -1
    line = line.strip()
    if iteration == 12:
        return joltage
    for i in range(largest_index,len(line)-11+iteration):
        if int(line[i])>int(largest) and i not in used:
            largest = line[i]
            largest_index = i
    used.append(largest_index)
    joltage += str(largest)
    return find_joltage_helper(iteration+1,line, used, joltage,largest_index)
print(find_largest_voltage_pt2('input3'))
            

