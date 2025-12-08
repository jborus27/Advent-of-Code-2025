count = 0

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

def print_grid(grid):
    for row in grid:
        row = ' '.join(row)
        print(row)

def move_rays(grid, row, col, used):
    global count
    
    if row == len(grid):
        return count

    if grid[row][col] == '.':
        grid[row][col] = '|'
        move_rays(grid,row+1,col, used)
        return
        
    if grid[row][col] == '^':
        if [row,col] not in used:
            used.append([row,col])
            count += 1
            move_rays(grid, row, col-1, used)
            move_rays(grid, row, col+1, used)
        return

    move_rays(grid,row+1,col, used)
    return

def split_rays(file):

    #turn the file into a 2d array
    grid = gridify(file)

    #store starting index
    starting_index = -1

    #find the start to the ray
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            starting_index = i
            break

    #move ray down
    #for each row in the grid:
    global count
    move_rays(grid,0,starting_index, [])

    return count

print(split_rays('input7'))
