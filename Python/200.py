class Solution:

    # Solution 1

    def dfs(self, grid: List[List[str]], i: int, j:int): 
        
        # If it is not the land anymore then return
        if i < 0 or i >= len(grid) or 
           j < 0 or j >= len(grid[0]) or
           grid[i][j] != '1':
               return 

        grid[i][j] = '0'
        
        # Search for North, East, South, West
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[9])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)

                    # search for every land and count up
                    count += 1
        return count
