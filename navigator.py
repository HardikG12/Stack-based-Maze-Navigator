from maze import *
from exception import *
from stack import *

class PacMan:
    
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
        
    
        
    # def find_path(self, start : tuple[int, int], end : tuple[int, int]) -> list[tuple[int, int]]:
    def find_path(self, start ,end ):
        
        # IMPLEMENT FUNCTION HERE
        if self.navigator_maze[start[0]][start[1]]==1 or self.navigator_maze[end[0]][end[1]]==1:
            raise PathNotFoundException
            
        visit = set()
        path = Stack()
        
        def dfs(curr):
            x = curr[0]
            y = curr[1]
            if not (x>=0 and x<len(self.navigator_maze) and y>=0 and y<len(self.navigator_maze[0])):
                return False
                
            if self.navigator_maze[x][y]==1:
                return False
                
            if curr==end:
                path.add(end)
                return True
                
            if curr in visit:
                return False
                
            visit.add(curr)
            path.add(curr)
            
            dir = [(0,-1),(1,0),(0,1),(-1,0)]
            
            for directions in dir:
                
                r = curr[0]+directions[0]
                c = curr[1]+directions[1]
                next_node = (r,c)
                if dfs(next_node):
                    return True
                    
            path.pop()
            return False
        if dfs(start)==True:
            l = []
            while not path.is_Empty():
                l.append(path.pop())
            l.reverse()
            print(l)
            return l
        raise PathNotFoundException