import numpy as np

def categorize_tp_pt_2(file):
    count = 1
    final_count = 0
    grid = gridify(file)
    while count > 0:
        returns = categorize_tp_pt_2_helper(file, grid)
        count = returns[0]
        grid = returns[1]
        final_count += count
    return final_count
    
def categorize_tp_pt_2_helper(file, tp_grid):
    count = 0
    for i in range(0,len(tp_grid[0])):
        for j in range(0,len(tp_grid)):
            if tp_grid[i][j] == '@':
                boolean = check_adjacent_squares(tp_grid,i,j)
                if boolean == True:
                    tp_grid[i][j] = 'x'
                    count += 1
    return [count, tp_grid]

def categorize_tp(file):
    tp_grid = gridify(file)
    count = 0
    for i in range(0,len(tp_grid[0])):
        for j in range(0,len(tp_grid)):
            if tp_grid[i][j] == '@':
                boolean = check_adjacent_squares(tp_grid,i,j)
                if boolean == True:
                    count += 1
    return count
                
    
def check_adjacent_squares(grid,i,j):
    count = 0
    if isValidPos(i-1,j, grid) and grid[i-1][j] == '@':
        count+=1
    if isValidPos(i,j-1, grid) and grid[i][j-1] == '@':
        count+=1
    if isValidPos(i-1,j-1, grid) and grid[i-1][j-1] == '@':
        count+=1
    if isValidPos(i+1,j-1, grid) and grid[i+1][j-1] == '@':
        count+=1
    if isValidPos(i+1,j, grid) and grid[i+1][j] == '@':
        count+=1
    if isValidPos(i+1,j+1, grid) and grid[i+1][j+1] == '@':
        count+=1
    if isValidPos(i,j+1, grid) and grid[i][j+1] == '@':
        count+=1
    if isValidPos(i-1,j+1, grid) and grid[i-1][j+1] == '@':
        count+=1
    if count<4: 
        return True
    else:
        return False

def isValidPos(i, j, grid):
    columns = len(grid[0])
    rows = len(grid)
    if j > rows-1 or j < 0:
        return False
    elif i > columns-1 or i < 0:
        return False
    else:
        return True
    
    
def gridify(file):
    fin = open(file)
    j = 0
    grid = []
    for line in fin:
        line = line.strip()
        new_row = []
        for i in range(0,len(line)):
            new_row.append(line[i])
        grid.append(new_row)
    return grid

#print(categorize_tp('inputcheck4.txt'))
print(categorize_tp_pt_2('input4'))
