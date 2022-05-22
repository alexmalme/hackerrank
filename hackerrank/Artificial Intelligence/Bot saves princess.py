def displayPathtoPrincess(n,grid):
    if grid[0][0] == 'p':
        print('UP\nLEFT\n'* ((n-1)//2))
    elif grid[n-1][0] == 'p':
        print('DOWN\nLEFT\n'* ((n-1)//2))
    elif grid[0][n-1] == 'p':
        print('UP\nRIGHT\n'* ((n-1)//2))
    elif grid[n-1][n-1] == 'p':
        print('DOWN\nRIGHT\n'* ((n-1)//2))
        
def displayPathtoPrincess2(n,grid):
    if grid[0][0]!="-": 
        q="UP\nLEFT\n"
    elif grid[0][n-1]!="-": 
        q="UP\RIGHT\n"
    elif grid[n-1][0]!="-": 
        q = "DOWN\nLEFT\n"
    else: 
        q="DOWN\nRIGHT\n"
    for i in range(n//2):
        print(q,end ="")
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)