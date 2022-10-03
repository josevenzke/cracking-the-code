
def getFood(area):
    q = [(0,0,0)]
    visited = set()
    visited.add((0,0))
    while q:
        x,y,count = q.pop(0)
        if area[x][y] == 9:
            return count
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i,j in directions:
            new_x = i+x
            new_y = j+y
            if new_x < 0 or new_y < 0 or new_x >=len(area) or new_y >= len(area[0]) or (new_x,new_y) in visited or area[new_x][new_y] == 0:
                continue
            q.append([new_x,new_y,count+1])
            visited.add((new_x,new_y))

    return -1


area = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,1,1],
        [1,0,0,1,0],
        [1,1,1,9,0]]

x = getFood(area)
print(x)