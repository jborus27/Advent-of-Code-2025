import math
import re

def cephalopod_math(file):
    fin = open(file)
    problems = []
    answers = []
    for line in fin:
        print('here')
        line = line.strip().split(' ')
        line = list(filter(lambda item: item != '', line))
        if len(problems) == 0:
            for i in range(len(line)):
                problems.append([])
        for i in range(len(line)):
            problems[i].append(line[i])
    for problem in problems:
        if '*' in problem:
            problem.pop(len(problem)-1)
            problem = [int(item) for item in problem]
            prod = math.prod(problem)
            answers.append(prod)
        else:
            problem.pop(len(problem)-1)
            problem = [int(item) for item in problem]
            prod = sum(problem)
            answers.append(prod)
    return sum(answers)
            
#print(cephalopod_math('input6'))

#split the string into different parts
##def split_string(string):
##    split = []
##    i = 0
##    temp_string = ""
##    while i<len(string):
##        if string[i] != ' ':
##            while i < len(string) and string[i] != ' ':
##                temp_string += string[i]
##                i+=1
##            split.append(temp_string)
##            temp_string = ''
##        elif string[i] == ' ':
##            if i-1 > 0 and string[i-1] != ' ':
##                i+=1
##            else:
##                temp_string += ' '
##                i+=1
##    return split

def split_string(string,column_width,lengths):
    split = []
    temp_string = ""
    i = 0
    while i<len(string):
        if '*' not in string and '+' not in string:
            temp_string = string[i:i+column_width]
            split.append(temp_string)
            i+=column_width+1
        else:
            split.append(string[i])
            i+=column_width+1
    return split

def find_column_lengths(last_line):
    print(last_line)
    m = 0
    count = 0
    lengths = []
    while m<len(last_line):
        print(m)
        count = 0
        if last_line[m] != ' ' and m < len(last_line):
            m+=1
            while last_line[m] == ' ' and m < len(last_line):
                m+=1
                count += 1
            lengths.append(count)
    return lengths

def cephalopod_math_pt_2(file, column_width):
    fin = open(file)
    problems = []
    answers = []
    last_line = fin.readlines()[len(fin.readlines())-1]

    lengths = find_column_lengths(last_line)
    print(lengths)
                
    for line in fin:
        #parse line
        line = line.replace('\n', '')
        line = split_string(line, 3, lengths)
        
        #if not the operations line
        if '*' not in line:
            
            if len(problems) == 0:
                for i in range(len(line)):
                    problems.append([])
                    
            #split numbers into digits
            for i in range(len(line)):
                line[i].split()
                if len(problems[i]) < len(line[i]):
                    for k in range(len(problems[i]),len(line[i])):
                        problems[i].append([])
                for j in range(len(line[i])):
                    if j != len(line[i]):
                        problems[i][j].append(line[i][j])
        
        #append operators seperately
        else:
            for i in range(len(line)):
                problems[i].append(line[i])
    
    #make everything into numbers
    for problem_index, problem in enumerate(problems):
        for number_index, number in enumerate(problem):
            if type(problems[problem_index][number_index]) != str:
                cur = problems[problem_index][number_index]
                cur = ''.join(cur)
                cur = cur.strip()
                problems[problem_index][number_index] = cur

    #use the same method as before to put everything together
    print(problems)
    for problem in problems:
        if '*' in problem:
            problem.pop(len(problem)-1)
            problem = [int(item) for item in problem]
            prod = math.prod(problem)
            answers.append(prod)
        else:
            problem.pop(len(problem)-1)
            problem = [int(item) for item in problem]
            prod = sum(problem)
            answers.append(prod)
    return sum(answers)

print(cephalopod_math_pt_2(('input6'), 4))



















