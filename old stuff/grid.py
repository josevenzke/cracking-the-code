def numIslands(grid) -> int:
    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid)
            if grid[i][j] == '1':
                num_islands+=1
                flip(i,j,grid)
    print(grid,num_islands)
    return num_islands


def flip(i,j,grid):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
        return
    if grid[i][j] == '1':
        grid[i][j] = '0'
        flip(i+1,j,grid)
        flip(i-1,j,grid)            
        flip(i,j+1,grid)            
        flip(i,j-1,grid)



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

numIslands(grid)